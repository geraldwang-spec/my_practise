import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.ptt.cc/bbs/nba/index.html'

headers = {
    "User-Agent": "Mozilla/5.0"
}

cookies = {
    "over18": "1"
}

# 抓網頁
res = requests.get(url, headers=headers, cookies=cookies)
soup = BeautifulSoup(res.text, 'lxml')
titles = soup.find_all("div", class_="title")

# 開 CSV 檔
with open("ptt_nba.csv", "w", newline='', encoding="utf-8-sig") as f:
    writer = csv.writer(f)

    # 寫標題列
    writer.writerow(["title", "link"])

    # 寫資料
    for t in titles:
        a_tag = t.find("a")
        if a_tag:
            title = a_tag.text.strip()
            link = "https://www.ptt.cc" + a_tag["href"]
        else:
            title = "已被刪除"
            link = "#"

        writer.writerow([title, link])

print(" CSV 已完成！")



