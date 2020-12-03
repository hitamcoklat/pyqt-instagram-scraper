import sys
import csv
import json
import time
import urllib.request
from urllib.error import HTTPError

class ShopifyScrape:

    def __init__(self, maxData):
        self.maxData = maxData
        self.userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

    def get_page(self, url, collection_handle=None):
        full_url = url
        if collection_handle:
            full_url += '/collections/{}'.format(collection_handle)
        full_url += '/products.json'
        req = urllib.request.Request(
            full_url + '?limit={}'.format(self.maxData),
            data=None,
            headers={
                'User-Agent': self.userAgent
            }
        )
        while True:
            try:
                data = urllib.request.urlopen(req).read()
                break
            except HTTPError:
                print('Blocked! Sleeping...')
                time.sleep(180)
                print('Retrying')

        products = json.loads(data.decode())['products']
        return products


    def get_page_collections(self, url):

        full_url = url + '/collections.json'
        print(full_url)

        req = urllib.request.Request(
            full_url,
            data=None,
            headers={
                'User-Agent': self.userAgent
            }
        )

        data = urllib.request.urlopen(req).read()
        cols = json.loads(data.decode())['collections']
        return cols

    def check_shopify(self, url):
        try:
            self.get_page(url, 1)
            return True
        except Exception:
            return False


    def fix_url(self, url):
        fixed_url = url.strip()
        if not fixed_url.startswith('http://') and \
           not fixed_url.startswith('https://'):
            fixed_url = 'https://' + fixed_url

        return fixed_url.rstrip('/')


    def extract_products_collection(self, url, col):

        products = self.get_page(url, col)

        while products:
            for product in products:
                title = product['title']
                product_type = product['product_type']
                product_url = url + '/products/' + product['handle']
                product_handle = product['handle']

                def get_image(variant_id):
                    images = product['images']
                    for i in images:
                        k = [str(v) for v in i['variant_ids']]
                        if str(variant_id) in k:
                            return i['src']

                    return ''

                for i, variant in enumerate(product['variants']):
                    price = variant['price'] or ''
                    option1_value = variant['option1'] or ''
                    option2_value = variant['option2'] or ''
                    option3_value = variant['option3'] or ''
                    option_value = ' '.join([option1_value, option2_value,
                                             option3_value]).strip()
                    sku = variant['sku'] or ''
                    main_image_src = ''
                    if product['images']:
                        main_image_src = product['images'][0]['src'] or ''

                    image_src = get_image(variant['id']) or main_image_src
                    stock = 'Yes'
                    if not variant['available']:
                        stock = 'No'

                    row = {'sku': sku, 'product_type': product_type,
                           'title': title, 'option_value': option_value,
                           'price': price, 'stock': stock, 'body': str(product['body_html']),
                           'variant_id': product_handle + str(variant['id']),
                           'product_url': product_url, 'image_src': image_src}

                    print(row)

                    for k in row:
                        row[k] = str(row[k].strip()) if row[k] else ''

                    yield row

    def extract_products_json(self, url,collections=None):

        seen_variants = set()
        for ci, col in enumerate(self.get_page_collections(url)):

            if collections and col['handle'] not in collections:
                continue

            handle = col['handle']
            title = col['title']

            resArray = list()
            for pi, product in enumerate(self.extract_products_collection(url, handle)):

                if len(resArray) == self.maxData:
                    return False

                variant_id = product['variant_id']

                if variant_id in seen_variants:
                    continue

                seen_variants.add(variant_id)

                listObject = {
                    'code': product['sku'],
                    'collection': str(title),
                    'category': product['product_type'],
                    'name': product['title'],
                    'variantName': product['option_value'],
                    'price': product['price'],
                    'inStock': product['stock'],
                    'URL': product['product_url'],
                    'imageURL': product['image_src']
                }

                resArray.append(listObject)

                yield listObject

    def main(self, url):
        url = self.fix_url(url)
        result = list()
        for i, res in enumerate(self.extract_products_json(url)):
            result.append(res)

        return result