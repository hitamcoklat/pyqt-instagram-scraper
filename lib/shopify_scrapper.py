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
        print(full_url)
        req = urllib.request.Request(
            full_url,
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
        dataProduk = list()
        for product in products:
            # print(product['variants'])
            title = product['title'] or ''
            product_type = product['product_type'] or ''
            product_url = url + '/products/' + product['handle'] or ''
            product_handle = product['handle'] or ''
            # print(title)
            def get_image(variant_id):
                images = product['images'] or ''
                for i in images:
                    k = [str(v) for v in i['variant_ids']]
                    if str(variant_id) in k:
                        return i['src'] or ''

                return ''

            for variant in product['variants']:
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

                dataProduk.append(row)

        return dataProduk

    def extract_products_json(self, url, collections=None):
        dataProduk = list()
        for col in self.get_page_collections(url):
            if collections and col['handle'] not in collections:
                continue
            handle = col['handle']
            title = col['title']
            no = 0
            for product in self.extract_products_collection(url, handle):
                listObject = {
                    'code': product['sku'] or '',
                    'collection': str(title) or '',
                    'category': product['product_type'] or '',
                    'name': product['title'] or '',
                    'variantName': product['option_value'] or '',
                    'price': product['price'] or '',
                    'inStock': product['stock'] or '',
                    'URL': product['product_url'] or '',
                    'imageURL': product['image_src'] or ''
                }
                no += 1
                dataProduk.append(listObject)
                if no == self.maxData:
                    return dataProduk

        return dataProduk

    def main(self, url):
        url = self.fix_url(url)
        result = list()

        for res in self.extract_products_json(url):
            result.append(res)

        return result