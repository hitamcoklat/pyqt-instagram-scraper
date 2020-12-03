from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import json
import cssutils

class ScrapeShopee(object):

    def initScrape():

        # options = webdriver.Firefox()
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--incognito')
        # options.add_argument('--headless')
        wd = webdriver.Firefox()

        wd.get("https://shopee.co.id/daily_discover?pageNumber=1")


        # Wait for the dynamically loaded elements to show up
        WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopee-page-controller")))

        html_page = wd.page_source
        # wd.quit()

        soup = BeautifulSoup(html_page, "lxml")

        dataLink = []
        # dataLink = ['https://shopee.co.id/🔥Ready-Stock-🔥Nibosi-2309s3-Jam-Tangan-Quartz-Mewah-Bahan-Stainless-Steel-Tahan-Air-i.95540047.1615174460', 'https://shopee.co.id/Bella-Square-warna-part-1--i.37132443.631161363']

        for a in soup.select('div.page-recommend__content a'):
            dataLink.append("https://shopee.co.id" + a['href'])

        objectData = []

        try:

            for ab in dataLink:

                wd.get(ab)

                # SCROLL_PAUSE_TIME = 3

                # Get scroll height
                time.sleep(2)
                wd.execute_script("window.scrollTo(0, 1000)")
                time.sleep(2)
                wd.execute_script("window.scrollTo(0, 2000)")
                time.sleep(2)
                wd.execute_script("window.scrollTo(0, 3000)")
                # time.sleep(3)
                # wd.execute_script("window.scrollTo(0, 10000)")


                WebDriverWait(wd, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "product-ratings")))

                html_page = wd.page_source

                soup = BeautifulSoup(html_page, "html.parser")

                try:
                    objectData.append({
                        'namaProduk': soup.select_one('div.qaNIZv').text,
                        'deskripsi': soup.select_one('div._2u0jt9').text,
                        'penilaian': soup.select_one('div._3mK1I2 > div:nth-child(1) > div > span').text,
                        'img1': soup.select_one('div.F3D_QV>div:nth-child(1)>div>div:nth-child(1)>div').attrs['style'].split("url(")[1].split(")")[0],
                        'img2': soup.select_one('div.F3D_QV>div:nth-child(2)>div>div:nth-child(1)>div').attrs['style'].split("url(")[1].split(")")[0],
                        'img3': soup.select_one('div.F3D_QV>div:nth-child(3)>div>div:nth-child(1)>div').attrs['style'].split("url(")[1].split(")")[0],
                        'img4': soup.select_one('div.F3D_QV>div:nth-child(4)>div>div:nth-child(1)>div').attrs['style'].split("url(")[1].split(")")[0],
                        'jmlFavorit': soup.select_one('div._25DJo1 > div').text,
                        'tersisa': soup.select_one('div._1FzU2Y>div:nth-child(2)>div:nth-child(2)').text,
                        'pengikut': soup.select_one('div._3mK1I2>div:nth-child(3)>div:nth-child(2)>span').text,
                        'terjual': soup.select_one('div._22sp0A').text
                    })
                except AttributeError:
                    pass

        except TimeoutException as ex:
            print("Exception has been thrown. " + str(ex))

        return objectData


# print(ScrapeShopee.initScrape())
# # print(json.dumps(ScrapeShopee.initScrape(), indent=4))
# # print(json.dumps(init(), indent=4))
