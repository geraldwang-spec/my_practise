import keyword
import requests
import streamlit as st
import folium
from streamlit_folium import st_folium

url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'

@st.cache_data
def fetch_data():
    return requests.get(url).json()

data = fetch_data()
st.title('youbike search system')

keywords = st.text_input('input keyword')

results=[]
if keywords:
    for s in data:
        if keywords in s.get('sna'):
            results.append(s)
    st.write(f"found = {len(results)}")
        # st.write(f"{s['sna']} = ${s['available_rent_bikes']}")

for s in results[:10]:
    st.write(
        s.get('sna'),
        "| 行政區",s.get('sarea'),
        "| 可借",s.get('available_rent_bikes'),
        "| 可還",s.get('available_return_bikes'),
        )


#========map
if len(results) >0:
    first=results[0]
    m=folium.Map(
        location=[first['latitude'],first['longitude']],
        zoom_start=13
    )
    for s in results[:10]:
        folium.Marker(
            location=[s['latitude'],s['longitude']],
            tooltip=s['sna']
        ).add_to(m)

    st.subheader('show map')
    st_folium(m, width=700, height=700)

