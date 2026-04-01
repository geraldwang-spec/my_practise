import requests
import streamlit as st

st.title('🚄🚄🚄高鐵查詢系統')

keyword=st.text_input('輸入起點(例如：台南)')

client_id='eelshop-eb0590ad-aeca-45f4'
client_secret='afb8f348-cdbb-4a75-b6e6-ebfa78279767'

auth_url='https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token'

authdata = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}

res = requests.post(auth_url, data=authdata)
token=res.json()['access_token']
print("token get OK")


url = "https://tdx.transportdata.tw/api/basic/v2/Rail/THSR/DailyTimetable/Today"
headers={
    'Authorization':f'Bearer {token}'
}

res=requests.get(url, headers=headers)
data=res.json()

for t in data:
    stops=t['StopTimes']
    for s in stops:
        station_name = s['StationName']['Zh_tw']
        if keyword and station_name == keyword:
            train_no = t['DailyTrainInfo']['TrainNo']
            
            arrive_time=s['ArrivalTime']
            depart_time=s['DepartureTime']

            depart=s['DepartureTime']
            origin=stops[0]['StationName']['Zh_tw']
            dest=stops[-1]['StationName']['Zh_tw']
            print(train_no, 
                  "到達", station_name, ":" ,arrive_time,
                  "離開", depart_time,
                  "起點", origin,
                  "終點", dest)
            st.write(train_no, 
                  "到達", station_name, ":" ,arrive_time,
                  "離開", depart_time,
                  "起點", origin,
                  "終點", dest)
            break


# for t in data:
#     stops=t['StopTimes']
#     origin=stops[0]['StationName']['Zh_tw']
#
#     if keyword and origin == keyword:
#         depart=stops[0]['DepartureTime']
#
#         dest=stops[-1]['StationName']['Zh_tw']
#         arrive=stops[-1]['DepartureTime']
#         train_no = t['DailyTrainInfo']['TrainNo']
#         print(train_no, origin, depart, dest, arrive)
#         st.write(train_no, origin, depart, dest, arrive)


