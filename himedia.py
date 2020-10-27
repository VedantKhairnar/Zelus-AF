from selenium import webdriver
from time import time, sleep
import logging
import json
from webdriver_manager.chrome import ChromeDriverManager

# time of start of scraping
start = time()

# List declared for storing data
data_HIMEDIA = []

# Get driver
def get_driver():
    #driver = getattr(threadLocal, 'driver', None)

    # Chrome DRiver options
    options = webdriver.ChromeOptions()
    #options = webdriver.FirefoxOptions()
    options.add_argument("--ignore-certificate-errors")
    #options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    #if driver is None:
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    driver.maximize_window()
        # setattr(threadLocal, 'driver', driver)

    return driver

######################################

######################################
# Scrapes and pushes the data in a json file
def HIMEDIA(driver, url):

    try:
        driver.get(url)
        sleep(3)
    except Exception as e:
        print(f'DRIVER ERROR : {e}')

    try:
        product_div = driver.find_elements_by_class_name('kuName')
        total_res = len(product_div)        # Number of results in actual
    except Exception as e:
        print(f'PRODCUT ERROR: {e}')
        pass

    try:
        product_prices = driver.find_elements_by_class_name('kuPrice')
    except Exception as e:
        print(f'PRODUCT PRICE ERROR: {e}')

    try:
        product_image = driver.find_elements_by_class_name('klevuImgWrap')
    except Exception as e:
        print(f'PRODUCT IMAGE ERROR: {e}')

    count = total_res
    flag = 0
    if total_res > 5:
        count = 5    # Number of results we want at max.
        flag = 1

    elif total_res==0 :
        flag = 0
        driver.quit()
        print("NO RESULT FOUND")
        return

    i = 0 #iterator
    while count<=total_res and i<=count:

        try:
            product_name = product_div[i].text
            print(product_name)
        except Exception as e:
            print(f"PRODUCT NAME: {e}")

        try:
            prod_price = product_prices[i].text
            print(prod_price)
        except Exception as e:
            print(f'PRICE NOT FOUND! SKIPPED!')
            count+=1
            i+=1
            continue

        try:
            prod_img = product_image[i].find_element_by_tag_name('a').find_element_by_tag_name('img').get_attribute(('src'))
            print(prod_img)
        except Exception as e:
            print(f'PRODCUT IMAGE ERROR: {e}')
            pass

        data1 = {
            'PRODUCT': product_name,
            'PRICE' : prod_price,
            'IMAGE': prod_img
        }

        data_HIMEDIA.append(data1)
        i+=1

    sleep(2)
    print(data_HIMEDIA)
    driver.quit()
    with open('data_himedia.json', 'w') as f:
        json.dump(data_HIMEDIA, f)

######################################

######################################
# Generates URL for query
def URL_Generator(driver, q):
    q = q.split(' ')

    # Remove any extra space in start or end
    for char in q:

        if char == '':
            q.remove(char)

    query = '+'.join(q)

    URL = f'https://www.himediastore.com/search/?q={q}'

    HIMEDIA(driver, URL)

    return

######################################

if __name__ == "__main__":
    driver = get_driver()

    # Input your query
    query = input('Query please: ')

    try:
        # Generate query URL
        URL_Generator(driver, query)
    except Exception as e:
        print(f'URL Generator ERROR: {e}')

    # End time of scrape
    print(time()-start)

