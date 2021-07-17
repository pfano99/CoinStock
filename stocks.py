from twelvedata import TDClient
from  secrets_info import twelve_api

class StockData:
    def __init__(self, api_key=twelve_api):
        self.td = TDClient(apikey=api_key)

    def get_stock(self, symbol='AAPL', interval='1min', timezone='America/New_York'):
        try:
            ts = self.td.time_series(
                    symbol=symbol,
                    interval=interval,
                    timezone=timezone,
                ).as_json()
            return ts
            
        except:
            return None
    
    def clean_data(self, symbol='AAPL', interval='1min', timezone='America/New_York'):
        data = self.get_stock(symbol='AAPL', interval='1min', timezone='America/New_York')
        r = []
        if data:
            for i in data:
                r.append({'close': i['close'], 'datetime': i['datetime']})
            return r
        else:
            return None
    
    @property
    def sock_list(self,):
        r = self.td.symbol_search()
        return r.as_json()


# c = StockData()
# print(c.get_stock())