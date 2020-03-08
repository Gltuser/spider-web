from selenium import webdriver
from bs4 import BeautifulSoup
import pymysql
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')

connection = pymysql.connect('localhost', user='root', password='0102003', database='spider')
cursor = connection.cursor()


def get_page(url):
    try:
        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get(url)
        wait = WebDriverWait(browser, 10)

        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ptab-0"]/div/div[2]/section/div')))
        button.click()

    except Exception as e:
        print(e)
        get_page(url)

    time.sleep(1)

    items = browser.find_elements_by_xpath('//*[@id="ptab-0"]/div/div[2]/section/a/div/span[2]')

    content = [i.text for i in items]
    return content


def save_to_topsearch(url):

    items = get_page(url)

    for i in items:
        try:
            print(i)
            insert = 'insert into topsearch(dt,content) values(%s,%s)'
            dt = time.strftime('%Y-%m-%d %X')
            cursor.execute(insert, (dt, i))
            connection.commit()
        except Exception as e:
            print(e)


def main(url):
    save_to_topsearch(url)


if __name__ == '__main__':
    url = 'https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1'
    main(url)





