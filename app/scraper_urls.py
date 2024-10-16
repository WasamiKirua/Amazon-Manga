from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import BaseWebDriver, WebDriver
from selenium.common.exceptions import NoSuchElementException

from app.notifications.INotification import INotification
import json
import time
import sqlite3
import os

db_name = '/opt/app/data/amazon-manga.db'

def sleep(seconds):
    time.sleep(seconds)


def runScraperUrls(driver: WebDriver, logic: INotification):
    #yourScrapedData = []

    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT id, url FROM urls")
        urls = cursor.fetchall()
        for url_tuple in urls:
            url_id = url_tuple[0]
            url = url_tuple[1]
            # print('***********************')
            # print('Query DB for added URLs')
            # print('***********************')
            # print(f'URL_id: {url_id} - URL: {url}')
            # print()

            driver.get(url)
            sleep(5)

            # Retrive Title
            v_n = driver.find_element(By.ID, 'productTitle')
            title = v_n.text
            # print('***************')
            # print(f'Title: {title}')
            # print('***************')
            # print()
            
            # Retrive Availability
            try:
                # Try to find the element with id 'outOfStock'
                driver.find_element(By.ID, 'outOfStock')
                # If found, set availability to 'No'
                availability = 'No'
            except NoSuchElementException:
                # If not found, the product is available
                availability = 'Yes'
            # print('*****************************')
            # print(f'Availability: {availability}')
            # print('*****************************')
            # print()

            # Retrive Price
            try:
                # Find the price element using JavaScript's querySelector
                price_element = driver.execute_script(
                    'return document.querySelector(".a-section.a-spacing-none.aok-align-center.aok-relative span.aok-offscreen")'
                )
                # If not Null
                if price_element:
                    # Get the text
                    price = driver.execute_script("return arguments[0].textContent", price_element)
                else:
                    # If price_element is None, set price to None
                    price = None
            except NoSuchElementException:
                # Catch exception if NoSuchElementException is raised
                price = None
                print(price)

            # print('***************')
            # print(f'Price: {price}')
            # print('***************')
            # print()
            
            # Retrive Rating
            try:
                rating = driver.find_element(By.ID, "acrPopover").text
                # print('*****************')
                # print(f'Rating: {rating}')
                # print('*****************')
                # print()
            except NoSuchElementException:
                rating = None

            # Retrive Trama
            try:
                book_description_div = driver.find_element(By.ID, "bookDescription_feature_div")
                trama = book_description_div.find_element(By.TAG_NAME, "span").text
            except NoSuchElementException:
                trama = None
                # print('***************')
                # print(f'Trama: {trama}')
                # print('***************')
                # print()
            
            # Retrive Cover
            try:
                image_element = driver.find_element(By.ID, 'landingImage')
                image_url = image_element.get_attribute('src')
            except NoSuchElementException:
                image_url = None
                # print('*******************')
                # print(f'Cover: {image_url}')
                # print('*******************')
                # print()
            
            volume_json = {
                "title": title,
                "url": url,
                "price": price,
                "availability": availability,
                "rating": rating,
                "trama": trama,
                "cover": image_url
            }

            #yourScrapedData.append(volume_json)

            # Store JSON locally, just for reference
            # with open(f'/opt/app/{title}.json', 'w', encoding='utf-8') as json_out:
            #     json.dump(yourScrapedData, json_out, ensure_ascii=False, indent=4)
            # print(f'/opt/app/{title}.json Stored')
            # print()
            try:
                cursor.execute('''
                INSERT INTO manga (title, url, price, availability, rating, trama, cover)
                VALUES (:title, :url, :price, :availability, :rating, :trama, :cover)
                ''', volume_json)
            except sqlite3.Error as e:
                print(e)
    
            conn.commit()
            sleep(2)

            delete_stmt = 'DELETE FROM urls WHERE id = ?'
            try:
                cursor.execute(delete_stmt, (url_id,))
                print(f'Url: {url} with ID: {url_id} deleted from DB')
            except sqlite3.Error as e:
                print(e)

            conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    sleep(10)

    #return yourScrapedData 