from dataclasses import dataclass
from datetime import datetime

@dataclass
class Stock:
    id:str
    tradeDate:int
    time:int
    flat:float
    floor:float
    ceil:float
    open:float
    high:float
    low:float
    close:float
    millionAmount:float
    previousClose:float
    previousVolume:float
    previousMillionAmount:float


    @property
    def trade_date(self)->str:
        dt:datetime = datetime.fromtimestamp(self.tradeDate / 1000)
        return dt.strftime('%Y-%m-%d')

    @property
    def time_date(self)->str:
        dt:datetime = datetime.fromtimestamp(timestamp=self.time/1000)
        return dt.strftime(format='%Y-%m-%d')

    def price_change(self)->float:
        if self.flat == 0:
            return 0.0
        return round(number=((self.close-self.flat)/self.flat)*100)
