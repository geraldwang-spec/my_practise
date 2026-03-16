# basedpyright: typeCheckingMode=standard, reportUnknownMemberAccess=false, reportUnknownVariableType=false, reportGeneralTypeIssues=false, reportMissingTypeArgument=false, reportCallIssue=false
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

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
    wantgoo()
