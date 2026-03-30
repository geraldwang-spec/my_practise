import requests
# import streamlit as st 
#加上地圖套件
# import folium
# from streamlit_folium import st_folium
import sqlite3

#台北市的youbike 即時資料
url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

data=requests.get(url).json()
conn = sqlite3.connect('youbike3.db')
cursor=conn.cursor()

cursor.execute("""
create table if not exists youbike(
id integer primary key autoincrement,
sna text,
sarea integer,
rent_bikes integer,
return_bikes integer
)
               """)

cursor.execute("delete from youbike")

for s in data[:10]:
    cursor.execute(
        "insert into youbike(sna,sarea,rent_bikes, return_bikes) values (?,?,?,?)",
        (
            s.get('sna'),
            s.get("sarea"),
            s.get('available_rent_bikes'),
            s.get('available_return_bikes')
        )
    )

conn.commit()
cursor.execute("select * from youbike")
for row in cursor.fetchall():
    print(row)

conn.close()

# one = data[0]
# cursor.execute(
#     "insert into youbike(sna,sarea, rent_bikes, return_bikes) values (?,?,?,?)", 
#     (one.get("sna"), one.get("sarea"),one.get('available_rent_bikes'),one.get('available_return_bikes'))
# )

# conn.commit()
#
#
#
#
# #抓資料
# @st.cache_data
# def fetch_data():
#     return requests.get(url).json()
#
# data=fetch_data()
#
# st.title('YOUBIKE 查詢系統')
#
# #輸入關鍵字
# keywords=st.text_input('請輸入站名關鍵字(例如:大安)')
#
# results=[]
#
# #如果有輸入
# if keywords:
#
#     for s in data:
#         if keywords in s.get('sna'):
#             results.append(s)
#     st.write(f'找到{len(results)}筆資料!!!')
#
# #顯示前10筆
# for s in results[:10]:
#     st.write(
#         s.get('sna'),
#         '| 行政區:',s.get('sarea'),
#         '| 可借:',s.get('available_rent_bikes'),
#         '| 可還:',s.get('available_return_bikes'),             
#
#         )
#
# #=======新增地圖
# if len(results) >0:
#     first= results[0]
#     #把第一筆的地理位置當成地圖中心點
#     m=folium.Map(
#         location=[first['latitude'],first['longitude']],
#         zoom_start=13        
#         )
#     for s in results[:10]:
#         folium.Marker(
#             location=[s['latitude'],s['longitude']],
#             tooltip=s['sna']
#
#             ).add_to(m)     
#
#
