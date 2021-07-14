from pycoingecko import CoinGeckoAPI


class CoinsData:
    def __init__(self,):
        self.cg = CoinGeckoAPI()

    def compare_coins(self, crypt_lists, currency):
        r = self.cg.get_price(ids=crypt_lists, include_market_chart=True, vs_currencies=currency)
        return r
    
    @property
    def popular_coins(self,):
        p_coins = ['bitcoin', 'litecoin', 'ethereum', 'bitcoin-cash', 'monero', 'dogecoin']
        r = self.cg.get_price(ids=p_coins, include_market_chart=True,include_24hr_vol = True, include_24hr_change=True, vs_currencies='zar')
        re = [
                {
                    "name": "Bitcoin",
                    "price": r['bitcoin']['zar'],
                    "currency" : "ZAR",
                    "change" : round(r['bitcoin']['zar_24h_change'], 2),
                    "volume" : round(r['bitcoin']['zar_24h_vol'], 2)
                },
                {
                    "name": "Bitcoin cash",
                    "price": r['bitcoin-cash']['zar'],
                    "currency" : "ZAR",
                    "change" : round(r['bitcoin-cash']['zar_24h_change'], 2),
                    "volume" : round(r['bitcoin-cash']['zar_24h_vol'], 2)
                },
                {
                    "name": "Dogecoin",
                    "price": r['dogecoin']['zar'],
                    "currency" : "ZAR",
                    "change" : round(r['dogecoin']['zar_24h_change'], 2),
                    "volume" : round(r['dogecoin']['zar_24h_vol'], 2)
                },
                {
                    "name": "Ethereum",
                    "price": r['ethereum']['zar'],
                    "currency" : "ZAR",
                    "change" : round(r['ethereum']['zar_24h_change'], 2),
                    "volume" : round(r['ethereum']['zar_24h_vol'], 2)
                },
                {
                    "name": "litecoin",
                    "price": r['litecoin']['zar'],
                    "currency" : "ZAR",
                    "change" : round(r['litecoin']['zar_24h_change'], 2),
                    "volume" : round(r['litecoin']['zar_24h_vol'], 2)
                },
                {
                    "name": "Monero",
                    "price": r['monero']['zar'],
                    "currency" : "ZAR",
                    "change" : round(r['monero']['zar_24h_change'], 2),
                    "volume" : round(r['monero']['zar_24h_vol'], 2)
                }
        ]

        return re

    @property
    def supported_coins(self):
        r = self.cg.get_exchanges_list()
        return r
    
    def coin_data(self, id, currency):
        r = self.cg.get_price(ids=id, vs_currencies=currency, include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)
        try:
            r['image'] = self.cg.get_coin_history_by_id(id, '11-07-2021')['image']['small']
        except:
            r['image'] = None
        return r

    def coin_history(self, id, date):
        r = self.cg.get_coin_history_by_id(id, date=date)
        return r

