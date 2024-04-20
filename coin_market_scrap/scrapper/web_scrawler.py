# from celery import shared_task
from celery import Celery
from celery.schedules import crontab

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import json

import requests

app = Celery()

def addData(data_list):
    url = 'http://localhost:8000/v1/api/api'
    payload_list=[]
    for idx,data in enumerate(data_list):
        print("22-> ",idx)
        payload = {
            "Name":
            data[2],
            "Price":
            data[3],
            "one_hr":
            data[4],
            "twenty_four_hr":
            data[5],
            "seven_days_hr":
            data[6],
            "market_cap":
            data[7],
            "volume":
            data[8],
            "circulating_supply":
            data[9],
        }
        payload_list.append(payload)

    json_data = json.dumps(payload_list)
    # Sending the POST request
    response = requests.post(url, json=json_data)

    # Checking the response status
    if response.status_code == 201:
        print("POST request successful!")
        print("Response:", response.text)
    else:
        print("POST request failed:", response.status_code)


@app.task(bind=True)
def web_scrawler(args):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)

    browser.get('https://coinmarketcap.com/')
    browser.maximize_window()

    try:
        count_div = browser.find_elements(
            by=By.XPATH, value="//span[@class='sc-f70bb44c-0 ixXzyr table_footer-left']")
        count_str = count_div[0].text.split(' ')[-1]
        print(count_str)
        # Get the height of the webpage
        page_height = browser.execute_script("return document.body.scrollHeight")

        # Define the scroll increment (adjust as needed)
        scroll_increment = 100  # pixels

        # Loop to scroll gradually to the end of the page
        for i in range(0, page_height, scroll_increment):
            browser.execute_script("window.scrollTo(0, {});".format(i))
            time.sleep(0.1)  # Adjust the sleep time as needed for desired scrolling speed

        columns = WebDriverWait(browser, 5).until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//table[@class='sc-14cb040a-3 dsflYb cmc-table  ']"))
        )
        columns_name = []
        columns_values = []
        each_crypto_list = []
        for inner_body in columns:
            tbodys = inner_body.find_elements(by=By.XPATH, value=".//tbody")
            theads = inner_body.find_elements(by=By.XPATH, value=".//thead")
            for thead in theads:
                trs = thead.find_elements(by=By.XPATH, value=".//tr")
                for tr in trs:
                    ths = tr.find_elements(by=By.XPATH, value=".//th")
                    for th in ths:
                        columns_name.append(th.text)

            for each_tbody in tbodys:
                trs = each_tbody.find_elements(by=By.XPATH, value=".//tr")
                for tr in trs:
                    columns_values = []
                    td = tr.find_elements(by=By.XPATH, value=".//td")
                    for each_td in td:
                        columns_values.append(each_td.text)
                    each_crypto_list.append(columns_values)
        
        print(len(each_crypto_list))
        addData(each_crypto_list)

    except Exception as e:
        print("Exception in fetching columns data", e)

    browser.quit()
