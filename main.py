"""
If errors occur, try downloading the latest version of chromedriver.
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent

ua = UserAgent()


def get_data_with_selenium(url):
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={ua.random}')
    options.add_argument('--disable-blink-features=AutomationControlled')

    service = Service('./chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        with open('index.html', 'w', encoding='utf-8') as file:
            file.write(driver.page_source)

        time.sleep(5)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    get_data_with_selenium('https://www.google.com/')
