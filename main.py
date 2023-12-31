import yfinance
import pandas as pd
import datetime

class StockScraper:
    def get_stock_info(self, ticker):
        output = yfinance.Ticker(ticker) 
        return output       
        
    def get_stock_information(self, ticker):
        data = self.get_stock_info(ticker)  
        output = []
            
        timestamp = datetime.datetime.now()
        try:
            last_price = data.fast_info['last_price']
            
        except Exception:
            last_price = None

        output = {"Company ticker": ticker,
                "Last Price": last_price,
                "Time Stamp": timestamp}
        
        return output
        
    def read_text_file(self):
        output = []
        with open("stockslist.txt",'r') as f:
            for line in f:
                output.append(line.upper().strip())
        return output
        
    def run(self):
        tickers = self.read_text_file()
        df = pd.DataFrame(columns=['Company ticker','Last Price'])
        for ticker in tickers:
            data_row = self.get_stock_information(ticker)
            df = df._append(data_row, ignore_index=True)
        
        df.to_excel("marketPrice.xlsx")
        df.to_csv('marketPrice.txt', sep='\t', index=False)
        
StockScraper().run()

