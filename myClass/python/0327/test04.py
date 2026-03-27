import requests
import streamlit as st
import folium
from streamlit_folium import st_folium


url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'

st.title('地圖顯示')

# taipe center
m=folium.Map(
    location=[25.033,121.565],
    zoom_start=13
)

st_folium(m, width=700, height=700)
