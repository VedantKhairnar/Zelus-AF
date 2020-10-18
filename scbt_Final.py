import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from multiprocessing.pool import ThreadPool, Pool
from webdriver_manager.chrome import ChromeDriverManager
import logging
import threading
from time import sleep, time
# requests, webdriver_manager, 
# start time of script
start = time()

# List for data storage
data_SCBT = []

# Event Logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Multiple thread initializer
threadLocal = threading.local()

######################################

'''
function: get_driver()
----------------------
Initializes driver with Chrome options
For different threads

:returns driver
'''


def get_driver():
    driver = getattr(threadLocal, 'driver', None)

    # Chrome DRiver options
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    if driver is None:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        setattr(threadLocal, 'driver', driver)

    return driver

######################################
'''
function: scrape_links
----------------------
links_use: URLs to scrape passed as a list

- For query based on PRODUCT CATEGORY
- Scrapes data about PRODUCT
- Calculates time taken to get the data

:returns None
'''
def scrape_links(links_use):

    # Call get_driver()
    try:
        driver = get_driver()
    except Exception as e:
        print(f'Webdriver: {e}')
        return

    # Open the passed URL in driver
    # and scroll down the end of page
    # to load all the content
    try:
        print(links_use)
        driver.get(links_use)
# driver.implicitly_wait(15)
        print("Successfully opened Website")
# time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    except Exception as e:
        print(f'Driver.get error: {e}')
        return

    # Get the <tbody> tag for the information about the product
    try:
        # sleep for 2 seconds to allow the content to load
        sleep(2)

        # try 3 XPATH in order to get the right content
        try:

            table_body = driver.find_element_by_xpath(
                '// *[ @ id = "santacruz"] / div[1] / div[1] / div[3] / div / div[2] / div[2] / div / table / tbody'
            )

        except:

            try:
                table_body = driver.find_element_by_xpath(
                    '// *[ @ id = "santacruz"] / div[1] / div[1] / div[3] / div[2] / div / table / tbody'
                )
            except:
                table_body = driver.find_element_by_xpath(
                    '// *[ @id = "santacruz"] / div[1] / div[1] / div[3] / div[2] / div[2] / div / table / tbody'
                )

        # find element <tr>
        table_rows = table_body.find_elements_by_tag_name('tr')

        # Get Image URL FOR THE PRODUCT
        Image = driver.find_element_by_tag_name('img').get_attribute('src')
#print(Image)

        # Get PRODUCT DETAILS
        for tr in table_rows:
            table_data = tr.find_elements_by_tag_name('td')
            Product_Name = table_data[0].text
            Catalog_Num = table_data[1].text
            Unit = table_data[2].text
            Price = table_data[3].text
            print(f'{Product_Name}\n{Catalog_Num}\n{Unit}\n{Price}')

            # Store as dictionary
            data = {
                'PRODUCT': Product_Name,
                'CATALOG': Catalog_Num,
                'UNIT': Unit,
                'PRICE': Price,
                'IMAGE': Image
            }

            # Append DATA to list data_SCBT
            data_SCBT.append(data)
#print(data_SCBT)

#
# with open('data.json', 'w') as f:
#     json.dump(data, f)

    except Exception as e:
        print(f'Content Error: {e}')

    # Total running time for each page
    print(f"Total Running Time: {time() - start} seconds")
    # Quit Driver
    driver.quit()
    return

#########################################

'''
function: main()
----------------
links = All the URLs for product query

- Initialize threading for First three URLs 

'''
def main(links):

    if len(links) < 3:
        length = len(links)
    else:
        length = 3

    # Threading
    ThreadPool(length).map(scrape_links, links[0:length])
    # Dump data to data.json file
    data_json = {
        'SCBT' : data_SCBT
    }
    with open('data.json', 'w') as f:
        json.dump(data_json, f)


######################################


######################################
'''
function: Product_URLs
-----------------------

URL- URL for search query

- GET all the relevant URLs for PRODUCT CATEGORY BASED QUERY
- Scrapes Data for PRODUCT BASED QUERY(if any)

'''
def Product_URLs(URL):
    '''
    Sending Request to URL and getting response
    '''

    # Sending response
    try:
        response = requests.get(URL)
        print(response.url)

        '''
        Scrape data for URLs not the same as expected.
        '''
        if URL != response.url:

            scrape_links(response.url)

            data_json = {
                'SCBT' : data_SCBT
            }
            with open('data.json', 'w') as f:
                json.dump(data_json, f)
            exit()


    except Exception as e:
        print(f'Response {e}\nTry Again!')
        URL_Generator()

    # getting source code
    try:
        soup = BeautifulSoup(response.text, 'lxml')
        source_code = soup.prettify()
# print(source_code)
    except Exception as e:
        print(f'Source Code {e}\nTry Again!')
        URL_Generator()

    # get <tr>
    try:
        products = soup.find_all('tr')
    except Exception as e:
        print(f'Get <tr> {e}\nTry Again!')

    data = list()
    # find parent <td>
    try:
        for product in products:
            data.append(product.find_all('td'))
            # print(data)

        data.remove(data[0])  # remove empty list
    except Exception as e:
        print(f'Parent <td> {e}\nTry Again!')

    links = list()
    # get links from child <td>
    try:
        for content in data:
            link = content[1].b.a['href']
            links.append(link)

        # Function CAll
        main(links)
    except Exception as e:
        print(f'Get Links {e}\nTry Again!')


######################################


######################################
def URL_Generator(query):
    # Enter Query
    # query = "Bleaching Powder"
    # query = input("Enter your query: ")

    # Manipulating query to pass in the url
    query = query.split(' ')

    # Remove any extra space in start or end
    for char in query:

        if char == '':
            query.remove(char)

    query = '%20'.join(query)

    # Pass query to URL
    url = f'https://www.scbt.com/search?Ntt={query}'
    print(url)

    # Function call for scraping
    Product_URLs(url)


######################################
# if __name__ == "__main__":
#     URL_Generator()
