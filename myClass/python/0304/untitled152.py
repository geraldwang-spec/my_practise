import csv
import requests
from bs4 import BeautifulSoup
# url='https://www.ptt.cc/bbs/nba/index.html'
url='https://ithelp.ithome.com.tw/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
}

data = []

try:
    max_pages=int(input('你要抓幾頁呢??? ').strip())
except:
    max_pages=2

for page in range(1, max_pages+1):
    new_page = url + "?page="+str(page)
    r=requests.get(new_page, headers=headers)
    print(f'status = {r.status_code} url = {new_page}')
    soup=BeautifulSoup(r.text,'html.parser')   
    posts=soup.select( 'div.qa-list')
    print(f"===== 第{page}頁 ====")
    for p in posts:
        title_tag = p.select_one('a.qa-list__title-link')
        title = title_tag.get_text(strip=True) if title_tag else '0'

        browse_tag = p.select('.qa-condition__count')
        browse = browse_tag[-1].get_text(strip=True) if browse_tag else '0'
        
        author_tag = p.select_one('a.qa-list__info-link')
        author = author_tag.get_text(strip=True) if author_tag else ''

        print(f"{author} | {browse:<5} | {title}")
        data.append([author, browse, title])
    

filename='pttnba_it.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(['作者', '瀏覽數', '標題'])
    writer.writerows(data)

print(f"{filename} 成功寫入")


