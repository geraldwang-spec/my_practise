# 暫時使用金鑰
#
# client_id='eelshop-eb0590ad-aeca-45f4'
# client_secret='afb8f348-cdbb-4a75-b6e6-ebfa78279767'
#
# auth_url=
# https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token
#
import requests


client_id='eelshop-eb0590ad-aeca-45f4'
client_secret='afb8f348-cdbb-4a75-b6e6-ebfa78279767'

auth_url='https://tdx.transportdata.tw/auth/realms/TDXConnect/protocol/openid-connect/token'

data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}

res = requests.post(auth_url, data=data)
token=res.json()['access_token']
print("token get OK")


url = "https://tdx.transportdata.tw/api/basic/v2/Rail/THSR/DailyTimetable/Today"
headers={
    'Authorization':f'Bearer {token}'
}

res=requests.get(url, headers=headers)
data=res.json()
print('total:',len(data))

print('first data:', data[0].keys())

for t in data[:5]:
    train_no=t['DailyTrainInfo']['TrainNo']
    # print(train_no)

    stops=t['StopTimes']
    origin=stops[0]['StationName']['Zh_tw']
    depart=stops[0]['DepartureTime']

    dest=stops[-1]['StationName']['Zh_tw']
    arrive=stops[-1]['DepartureTime']
    print(train_no, origin, depart, dest, arrive)

