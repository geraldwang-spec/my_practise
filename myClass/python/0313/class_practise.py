# basedpyright: typeCheckingMode=standard, reportUnknownMemberAccess=false, reportUnknownVariableType=false, reportGeneralTypeIssues=false, reportMissingTypeArgument=false, reportCallIssue=false
from dataclasses import dataclass
from math import e
import time
from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests
from requests import Response
from datetime import datetime

@dataclass
class Stock:
    id:str
    tradeData:int

    @property
    def trade_Data(self)->str:
        dt:datetime = datetime.fromtimestamp(self.tradeData / 1000)
        return dt.strftime('%Y-%m-%d')


def request_practise()->None:
    url:str = "https://www.wantgoo.com/investrue/all-quote-info"
    headers:dict[str,str] = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        "Referer":"https://www.wantgoo.com/stock/ranking/top-gainer"
    }

    try:
        response:Response = requests.get(url=url, headers=headers)
        if response.status_code != 200:
            print(f"get data fail: {response.status_code}")
            return

        all_stocks:Any = response.json()
        print(f"len = {len(all_stocks)}")
        
        # ss:Stock = Stock(id='ddd',tradeData=232323)


    except Exception as e:
        print(f"Error Message={e}")


def sub_number(url:str)->str:
    #options:Options = Options()
    #options.add_argument(argument="--headless")
    #options.add_argument(argument="--disable-gpu")
    #options.add_argument(argument="--no-sandbox")
    #driver = webdriver.Chrome(options=options)
    driver = webdriver.Firefox()
    driver.get(url)
    wait = WebDriverWait(driver=driver, timeout=10)
    box:WebElement = wait.until(method=EC.presence_of_element_located(locator=(By.CSS_SELECTOR, "input[type='text']")))

    item = driver.find_element(By.CSS_SELECTOR, 'ul li a span.mr-1')
    print(f"len = {len(item)}")
    return "end"
    


def wantgoo()->None:
    print("wantgoo")
    #options:Options = Options()
    #options.add_argument(argument="--headless")
    #options.add_argument(argument="--windows-size=1920,1080")
    #options.add_argument(argument="user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    #options.add_argument(argument="--disable-gpu")
    #options.add_argument(argument="--no-sandbox")
    #driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    driver.get('https://www.wantgoo.com/stock/ranking/top-gainer')
    
    wait = WebDriverWait(driver, timeout=10)
    # box:WebElement =wait.until(method=EC.presence_of_element_located(locator=(By.CSS_SELECTOR, "input[type='text']")))
    
    box:WebElement =wait.until(method=EC.presence_of_element_located(locator=(By.CSS_SELECTOR, "input[type='text']")))
    trs= driver.find_elements(By.CSS_SELECTOR, 'tr')
    # print(f"counts = {len(trs)}")
    for tr in trs:
        tds = tr.find_elements(By.CSS_SELECTOR, 'td')
        # print(f"tds = {len(tds)}")
        if tds:
            link = tds[1].find_element(By.CSS_SELECTOR, "a[href*='/stock/']")
            url:str = link.get_attribute('href')
            print(f"url={url}")
            # _ = sub_number(url=url)
            print(f"{tds[0].text} | {tds[1].text} | {tds[2].text} | {link.get_attribute('href')}") 


if __name__ == "__main__":
    # wantgoo() # higher fail rate
    request_practise()
