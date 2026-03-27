import requests
import streamlit as st

url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'

data = requests.get(url).json()
print(len(data))

print(data[0],"\n")
print(data[0]['sna'], "......", data[0]['ar'])


print(data[100]['sna'], "......", data[100]['ar'])

for s in data[:10]:
    print(s['sna'], "可借:", s['available_rent_bikes'])
print('\n')
for s in data:
    if s['sarea'] == '台南':
        print(s['sna'],
              '可借', s['available_rent_bikes'])
