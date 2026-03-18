from unittest import result
import requests
from typing import Any
from requests import Response
from urllib3 import response
from .stock_module import Stock

def dict_to_class[T](cls: type[T], data: dict[str, object]) ->T:
    from dataclasses import fields, is_dataclass
    if not is_dataclass(obj=cls):
        raise TypeError(f"{cls} must be dataclasses")
    target_fields:set[str] = {f.name for f in fields(class_or_instance=cls)}
    filtered_data:dict[str,object] = {k: data.get(k,0) for k in target_fields}
    return cls(**filtered_data)

class stock_process:
    def __init__(self) -> None:
        pass

    def process_stocks(self, all_json:list[dict[str,object]])->list[Stock]:
        stock_object:list[Stock]=[]
        for i, s_dict in enumerate(all_json, 0):
            obj:Stock = dict_to_class(Stock, s_dict)
            stock_object.append(obj)
            row_data = " | ".join(map(str, vars(obj).values()))
            print(f"{i} | {row_data}")
    
        return stock_object

    def all_stock_current_data(self)->None:
        url:str = "https://www.wantgoo.com/investrue/all-quote-info"
        headers:dict[str,str] = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
            "Referer":"https://www.wantgoo.com/stock/ranking/top-gainer"
        }
     
        try:
            response:Response = requests.get(url=url, headers=headers)
            if response.status_code != 200:
                print(f"get data fail: {response.status_code}")
                return
    
            all_stocks:Any = response.json()
            print(f"len = {len(all_stocks)}")
            stocks:list[Stock] = self.process_stocks(all_json=all_stocks)
        except Exception as e:
            print(f"Error Message={e}")

    def all_stock_data(self)->None:
        url:str = "https://api.finmindtrade.com/api/v4/data?dataset=TaiwanStockInfo"
        headers:dict[str,str] = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        }

        try:
            response:Response = requests.get(url=url, headers=headers)
            if response.status_code != 200:
                print(f"get FindMind fail: {response.status_code}")
                return

            result:Any = response.json()
            if result.get('msg') != "success":
                print(f"findmind API fail: {result.get('status')}")
                return



        except Exception as e:
            print(f"Error Message={e}")
    
