from selenium import webdriver
from app.scraper import runScraper
from app.scraper_urls import runScraperUrls
from app.notifier import logic

def run_urls():
    yourScrapedDataUrls = None

    ff_options = webdriver.FirefoxOptions()
    ff_options.add_argument('--no-sandbox')
    ff_options.add_argument('--disable-dev-shm-usage')

    try:
        # DONT CHANGE THIS LINE
        driver_urls = webdriver.Remote("http://localhost:4444/wd/hub", options=ff_options)
        yourScrapedDataUrls = runScraperUrls(driver_urls, logic)


    except Exception as e:
        print(e)
        logic.crashed(e)
    finally:
        driver_urls.quit()
    return yourScrapedDataUrls

def run_scaper():
    yourScrapedData = None

    ff_options = webdriver.FirefoxOptions()
    ff_options.add_argument('--no-sandbox')
    ff_options.add_argument('--disable-dev-shm-usage')

    try:
        # DONT CHANGE THIS LINE
        driver = webdriver.Remote("http://localhost:4444/wd/hub", options=ff_options)
        yourScrapedData = runScraper(driver, logic)


    except Exception as e:
        print(e)
        logic.crashed(e)
    finally:
        driver.quit()
    return yourScrapedData

try:
    logic.start()
    urls = run_urls()
    data = run_scaper()
    logic.finished(urls)
    logic.finished(data)
except Exception as e:
    logic.crashed(e)
    print(e)

