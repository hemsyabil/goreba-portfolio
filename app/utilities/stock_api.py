# utilities/stock_api.py
import requests

class StockAPI:
    def __init__(self, api_key):
        self.base_url = "https://www.alphavantage.co/query"
        self.api_key = api_key
        
    def get_quote(self, symbol):
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": self.api_key
        }
        response = requests.get(self.base_url, params=params)
        return response.json()