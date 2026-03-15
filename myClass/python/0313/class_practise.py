from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.wantgoo.com/stock/ranking/top-gainer')

wait = WebDriverWait(driver, 10)
box = (EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']")))

trs = driver.find_elements(By.CSS_SELECTOR, 'tr')
# print(f"counts = {len(trs)}")
for tr in trs:
    tds = tr.find_elements(By.CSS_SELECTOR, 'td')
    # print(f"tds = {len(tds)}")
    if tds:
        link = tds[1].find_element(By.CSS_SELECTOR, "a[href*='/stock/']")
        print(f"{tds[0].text} | {tds[1].text} | {tds[2].text} | {links.get_attribute('href')}") 


