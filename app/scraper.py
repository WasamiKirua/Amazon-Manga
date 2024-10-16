from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import BaseWebDriver, WebDriver
from selenium.common.exceptions import NoSuchElementException

from app.notifications.INotification import INotification
import time
import sqlite3

db_name = '/opt/app/data/amazon-manga.db'

def sleep(seconds):
    time.sleep(seconds)

def runScraper(driver: WebDriver, logic: INotification):
    yourScrapedData = []

    # conn = None
    # try:
    #     conn = sqlite3.connect(db_name)
    #     cursor = conn.cursor()
    #     cursor.execute("SELECT id, url FROM urls")
    #     urls = cursor.fetchall()
    #     for url_tuple in urls:
    #         url_id = url_tuple[0]
    #         url = url_tuple[1]
    #         print('***********************')
    #         print('Query DB for added URLs')
    #         print('***********************')
    #         print(f'URL_id: {url_id} - URL: {url}')
    #         print()

    # except sqlite3.Error as e:
    #     print(e)
    # finally:
    #     if conn:
    #         conn.close()

    # #### YOUR CODE HERE ####
    # driver.get("https://www.amazon.de/dp/8828760869")

    # sleep(7)

    # v_n = driver.find_element(By.ID, 'productTitle')
    # title = v_n.text
    # print(f'Title: {title}')

    # try:
    #     # Try to find the element with id 'outOfStock'
    #     driver.find_element(By.ID, 'outOfStock')
    #     # If found, set availability to 'No'
    #     availability = 'No'
    # except NoSuchElementException:
    #     # If not found, the product is available
    #     availability = 'Yes'

    # print(f'Availability: {availability}')

    # try:
    #     # Find the price element using JavaScript's querySelector
    #     price_element = driver.execute_script(
    #         'return document.querySelector(".a-section.a-spacing-none.aok-align-center.aok-relative span.aok-offscreen")'
    #     )
    #     # If not Null
    #     if price_element:
    #         # Get the text
    #         price = driver.execute_script("return arguments[0].textContent", price_element)
    #     else:
    #         # If price_element is None, set price to None
    #         price = None
    # except NoSuchElementException:
    #     # Catch exception if NoSuchElementException is raised
    #     price = None
    #     print(f'Price: {price}')

    # try:
    #     # Rating element
    #     rating = driver.find_element(By.ID, "acrPopover").text
    #     print(f'Rating: {rating}')
    # except NoSuchElementException:
    #     rating = None

    # try:
    #     # Trama of volume
    #     book_description_div = driver.find_element(By.ID, "bookDescription_feature_div")
    #     trama = book_description_div.find_element(By.TAG_NAME, "span").text
    # except NoSuchElementException:
    #     trama = None
    # print(f'Trama: {trama}')

    # try:
    #     # Volume Cover 
    #     image_element = driver.find_element(By.ID, 'landingImage')
    #     image_url = image_element.get_attribute('src')
    # except NoSuchElementException:
    #     image_url = None
    # print(f'Cover: {image_url}')

    # volume_json = {
    #     "title": title,
    #     "url": "",
    #     "price": price,
    #     "availability": availability,
    #     "rating": rating,
    #     "trama": trama,
    #     "cover": image_url
    # }

    # yourScrapedData.append(volume_json)

    # sleep(2)

    return yourScrapedData