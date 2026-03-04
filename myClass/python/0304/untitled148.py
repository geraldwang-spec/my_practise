
import requests
from bs4 import BeautifulSoup
# url='https://www.ptt.cc/bbs/nba/index.html'
# url = 'https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
#     "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
# }
headers = {    'User-Agent':'Mozilla/.0'} # basic
cookies={'over18':'1'}

#CSS選擇器  class="r-ent" , 選擇器的上下階層是用 . 隔開

#先說要抓幾頁
try:
    max_pages=int(input('你要抓幾頁呢???').strip())
    
except:    
    max_pages=2 #使用者輸入亂掉就預設兩頁
    
for page in range(1,max_pages+1):
    r=requests.get(url, headers=headers, cookies=cookies)
    soup=BeautifulSoup(r.text,'html.parser')   #=================================re, r 要確認
    print(f'=====第{page}頁========')
    
    #CSS選擇器  class="r-ent" , 選擇器的上下階層是用 . 隔開
    posts=soup.select('div.r-ent') 
    
    for p  in posts:
        
        #等待修改 
        title_tag=p.select_one('.title a')
        author_tag=p.select_one('.author') 
        nrec_tag=p.select_one('.nrec span')   
        
        title= title_tag.get_text(strip=True) if title_tag else "" 
        author= author_tag.get_text(strip=True) if author_tag else ""  
        nrec= nrec_tag.get_text(strip=True) if nrec_tag else ""  
            
        print(f'{nrec:>3}  |{author:<12} | {title} ')
        # A if 條件 else B
    btns=soup.select('div.btn-group-paging a')    
    prev_url=None

    for b in btns:
        if '上頁' in b.get_text():
            prev_url='https://www.ptt.cc/'+ b['href']  #屬性
            break
        
    #如果沒有上頁，就提前結束
    if not prev_url:
        print('\n找不到上頁，提前結束')
        break
        
    #用上一頁來取代目前頁面，就可以無限循環
    url=prev_url    

