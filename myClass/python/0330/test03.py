
import keyword
import requests
import streamlit as st 
#加上地圖套件
# import folium
# from streamlit_folium import st_folium
import sqlite3

st.title("youbike search system")

#台北市的youbike 即時資料
url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

data=requests.get(url).json()
conn = sqlite3.connect('youbike3.db')
cursor=conn.cursor()

keyword=st.text_input('please input key words of station')

if keyword:
    cursor.execute("""
        select sna, sarea, rent_bikes, return_bikes from youbike
        where sna like ?
      """, ("%"+keyword+"%",))
    results=cursor.fetchall()
    st.write(f"found {len(results)}")

    for row in results:
        st.write(
            f"{row[0]} | {row[1]} | rent {row[2]} | return_bikes: {row[3]}"
        )
conn.close()

