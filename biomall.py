from selenium import webdriver
from time import time, sleep
import json
import logging
from webdriver_manager.chrome import ChromeDriverManager
import threading
from multiprocessing.pool import ThreadPool, Pool
import pprint


class BIOMALL:

    def __init__(self, query):

        self.path = 'chromedriver'  # CHROMEDRIVER PATH

        self.start = time()  # RECORD THE TIME WHEN SCRAPING START

        self.dataBiomall = {}

        # Event Logger
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        self.threadLocal = threading.local()  # MULTIPLE THREAD INITIALIZER

        self.query = query

        self.url = self.url_generator()  # GENERATE URL FROM QUERY

        self.scrape(url=self.url)

        pprint.pprint(self.dataBiomall)

        with open('dataBiomall.json', 'w') as f:
            json.dump(self.dataBiomall, f)

        # Total running time for BIOMALL
        print(f"Total Running Time: {int(time() - self.start)} seconds")

    def get_driver(self):

        # Chrome Driver options
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--incognito")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(executable_path=self.path, options=options)

        if driver is None:

            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            setattr(self.threadLocal, 'driver', driver)

        return driver

    def url_generator(self):

        q = self.query
        q = q.split(' ')

        # Remove any extra space in start or end
        for char in q:
            if char == '':
                q.remove(char)

        q = '%20'.join(q)

        url = []
        for i in range(1,4):
            url.append(f'https://www.biomall.in/search/{i}?query={q}')

        return url

    def scrape(self, url):

        try:
            self.driver = self.get_driver()  # INITIALIZE CHROME DRIVER
        except Exception as e:
            print(f'DRIVER INITIALIZATION ERROR: \n{e}')

        driver = self.driver
        # driver = getattr(self.threadLocal, 'driver', driver)

        for i in range(0,3):

            try:

                driver.get(url[i])  # open url in driver
                sleep(3)

            except Exception as e:

                print(f'DRIVER ERROR: {e}')

            if i == 0:
                try:

                    currency = driver.find_element_by_class_name('select-currency')
                    select_opt = currency.find_element_by_tag_name('label') \
                        .find_element_by_tag_name('select')
                    select_opt.click()
                    options = select_opt.find_elements_by_tag_name('option')

                    for option in options:

                        value = option.get_attribute('value')
                        if value == "INR":
                            option.click()
                            break
                    # sleep(7)

                except Exception as e:

                    print(f'CURRENCY ERROR: {e}')

                try:
                    driver.get(url[i])
                except Exception as e:
                    print(f"GET URL ERROR: {e}")

            try:

                products = driver.find_elements_by_class_name('category-col')

            except Exception as e:

                print(f'PRODUCTS ERROR: \n{e}')

            for item in products:

                try:

                    product_url = item.find_element_by_class_name('product-item') \
                        .find_element_by_tag_name('a')

                    product_image = product_url.find_element_by_tag_name('img').get_attribute('src')

                    product_title = product_url.find_element_by_tag_name('h2').text

                except Exception as e:

                    print(f'PRODUCT IMAGE/TITLE ERROR: \n{e}')

                try:

                    product_price = item.find_element_by_class_name('special-price') \
                        .find_element_by_tag_name('span').text
                    print(product_price)

                except Exception as e:

                    print(f'PRODUCT PRICE ERROR: \n{e}')

                try:

                    p_tags = item.find_elements_by_tag_name('p')
                    count = 1

                    for tag in p_tags:

                        if count == 1:
                            tmp = tag.text
                            product_brand = tmp.split(":")[1].lstrip(" ")
                            print(product_brand)

                        elif count == 2:
                            tmp = tag.text
                            product_catalog = tmp.split(":")[1].lstrip(" ")
                            print(product_catalog)

                        elif count == 3:
                            tmp = tag.text
                            product_quantity = tmp.split(":")[1].lstrip(" ")
                            print(product_quantity)

                        else:
                            break

                        count += 1

                except Exception as e:

                    print(f'PRODUCT BRAND/CATALOG/QUANTITY ERROR: \n{e}')

                if product_brand in self.dataBiomall:

                    self.dataBiomall[product_brand].append(
                        {
                            'PRODUCT': product_title,
                            'CATALOG': product_catalog,
                            'UNIT': product_quantity,
                            'PRICE': product_price,
                            'IMAGE': product_image
                        }
                    )

                else:

                    self.dataBiomall.update(
                        {
                            product_brand: [
                                {
                                    'PRODUCT': product_title,
                                    'CATALOG': product_catalog,
                                    'UNIT': product_quantity,
                                    'PRICE': product_price,
                                    'IMAGE': product_image
                                }
                            ]
                        }
                    )

                print('\n>>>>>>>>>>>>>>>>>>>>>\n')


        driver.quit()



if __name__ == '__main__':
    
    query = input("ENTER PRODUCT NAME: ")
    BIOMALL(query=query)




