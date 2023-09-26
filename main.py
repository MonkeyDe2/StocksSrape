import yfinance
import pandas as pd

class StockScraper:
    def get_stock_info(self, ticker):
        output = yfinance.Ticker(ticker) 
        return output       
        
    def get_stock_information(self, ticker):
        data = self.get_stock_info(ticker)  
        output = []
        
        output = {"Company ticker": ticker,
                "Previous close": data.fast_info['previousClose'],
                "Open": data.fast_info['open'],
                "Year high": data.fast_info['yearHigh'],
                "Year low": data.fast_info['yearLow']}
        
        return output
        
    def read_text_file(self):
        output = []
        with open("stocks.txt",'r') as f:
            for line in f:
                output.append(line.upper().strip())
        return output
        
    def run(self):
        tickers = self.read_text_file()
        df = pd.DataFrame(columns=['Company ticker','Previous close','Open','Year high','Year low'])
        for ticker in tickers:
            data_row = self.get_stock_information(ticker)
            df = df._append(data_row, ignore_index=True)
        
        df.to_excel("output.xlsx")
            
StockScraper().run()