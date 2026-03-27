from ssl import Options
from tkinter import wantobjects
from unittest import result
from flask import Flask
from flask.json import jsonify
import requests
from typing import Any, Optional
from requests import Response
from urllib3 import response
from .stock_module import Stock, StockData

def dict_to_class[T](cls: type[T], data: dict[str, object]) ->T:
    from dataclasses import fields, is_dataclass
    if not is_dataclass(obj=cls):
        raise TypeError(f"{cls} must be dataclasses")
    target_fields:set[str] = {f.name for f in fields(class_or_instance=cls)}
    filtered_data:dict[str,object] = {k: data.get(k,0) for k in target_fields}
    return cls(**filtered_data)

class stock_process_module:
    def __init__(self) -> None:
        pass

    def is_target_stock(self, stock_id: str, industry: str) -> bool:
        # 1. 過濾權證：長度 > 5 或是產業類別是 "所有證券"
        if len(stock_id) > 5 or industry == "所有證券":
            return False
            
        # 2. 過濾特別股：檢查代碼是否包含英文 (例如 2881A)
        # isdigit() 會在包含字母時回傳 False
        if not stock_id.isdigit():
            return False
            
        # 3. 過濾 REITs (受益證券)
        if industry == "受益證券":
            return False
            
        # 剩下的通常就是普通股、ETF 或 TDR
        return True

    def process_stocks(self, all_json:list[dict[str,object]])->list[Stock]:
        stock_object:list[Stock]=[]
        for i, s_dict in enumerate(all_json, 0):
            obj:Stock = dict_to_class(Stock, s_dict)
            stock_object.append(obj)
            # row_data = " | ".join(map(str, vars(obj).values()))
            # print(f"{i} | {row_data}")
    
        return stock_object

    def all_stock_current_data(self)->list[Stock] | None:
        stocks:list[Stock] = []
        url:str = "https://www.wantgoo.com/investrue/all-quote-info"
        headers:dict[str,str] = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
            "Referer":"https://www.wantgoo.com/stock/ranking/top-gainer"
        }
     
        try:
            response:Response = requests.get(url=url, headers=headers)
            if response.status_code != 200:
                print(f"get data fail: {response.status_code}")
                return None

            all_stocks:Any = response.json()
            # print(f"len = {len(all_stocks)}")
            stocks: list[Stock]= self.process_stocks(all_json=all_stocks)
        except Exception as e:
            print(f"Error Message={e}")
            return None

        return stocks

    def all_stock_data(self)->list[StockData] | None:
        stock_object:list[StockData]=[]
        url:str = "https://api.finmindtrade.com/api/v4/data?dataset=TaiwanStockInfoWithWarrant"
        headers:dict[str,str] = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        }

        try:
            response:Response = requests.get(url=url, headers=headers)
            if response.status_code != 200:
                print(f"get FindMind fail: {response.status_code}")
                return None

            result:Any = response.json()
            if result.get('msg') != "success":
                print(f"findmind API fail: {result.get('status')}")
                return None 

            get_data:list[dict[str,object]] = result.get('data')
            for s_dict in get_data:
                # if self.is_target_stock(stock_id=str(s_dict['stock_id']), industry=str(s_dict['industry_category'])) == True:
                #     continue
                obj:StockData = dict_to_class(cls=StockData,data= s_dict)
                stock_object.append(obj)

            # print(f"len stocks= {len(stock_object)}")

        except Exception as e:
            print(f"Error Message={e}")
            return None

        return stock_object
    
    def top_gainer_stock_tw(self, tw_stock:list[Stock])->list[Stock]:
        # log_data:str = ""
        change_sorts:list[Stock] = sorted(tw_stock, 
                                        key=lambda s: s.price_change(),
                                        reverse = True)

        # for i, s in enumerate(change_sorts[:10]):
        #     # log_data +=f"{i} | {s.id} | {s.stockData.stock_name} | {s.price_change()}\n" 
        #     print(f"{i} | {s.id} | {s.stockData.stock_name} | {s.price_change()}")
        #
        
        # with open("stock.txt", "w", encoding="utf-8") as f:
        #     f.write(log_data)
        return change_sorts


    def process_stocks_data(self, select:int)->list[dict[str,str]]:
        wnatgoo_data:list[Stock] | None = self.all_stock_current_data()
        if wnatgoo_data is None:
            print("wantgoo.com get data fail")
            return
        stock_datas:list[StockData] | None = self.all_stock_data()

        if stock_datas  is None:
            print("FindMind get data fail")
            return

        # 2. 進行配對
        fm_map:dict[str, StockData] = {s.stock_id: s for s in stock_datas} # 用 dict 效能更好
    
        for s_obj in wnatgoo_data:
            s_obj.stockData = fm_map.get(s_obj.id)

        # 3. 分類：成功對應的 vs 找不到的
        # 真正成功的台股
        valid_stocks:list[Stock] = [s for s in wnatgoo_data if s.stockData is not None]
        # 你剛才看到的那些未知標的
        unknown_stocks:list[Stock] = [s for s in wnatgoo_data if s.stockData is None]

        # # 印出前 10 筆成功的標的
        # print("--- 成功對應的股票 ---")
        # for i, s in enumerate(valid_stocks):
        #     # 這裡因為上面 filter 過了，s.stockData 絕對不是 None
        #     print(f"{i} | {s.id} | {s.stockData.stock_name}")
        #
        # # 印出前 10 筆未知的標的
        # print("\n--- 未知標的 (指數/權證/美股) ---")
        # for i, s in enumerate(unknown_stocks[:10]):
        #     print(f"{i} | {s.id} | unknow")
        sample_data:list[dict[str, str]] = []
        if select == 0:
            show_stocks:list[Stock] = self.top_gainer_stock_tw(tw_stock=valid_stocks)

            for i, s in enumerate(show_stocks[:100]):
                stock_info:dict[str,str] ={
                    "number":str(i),
                    "id":str(s.id),
                    "name":str(s.stockData.stock_name),
                    "price":str(s.price_change())
                }
                 
                sample_data.append(stock_info)

        return sample_data   



        


        





    

