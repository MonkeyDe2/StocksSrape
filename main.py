import yfinance as yf
import pandas as pd
import datetime
import time

class StockScraper:
    def get_stocks_information(self, tickers):
        price_out = []
        time_out = []
        ticker_out = []

        ytick_format = ' '.join(tickers)

        yf_ticks = yf.Tickers(ytick_format)
        for ticker in tickers:
            try: 
                price_out.append(yf_ticks.tickers[ticker].fast_info['last_price'])
                time_out.append(datetime.datetime.now())
                ticker_out.append(ticker_out)
            except Exception as e:
                print(datetime.datetime.now(), f'|ERROR for ticker symbol {ticker}. Ignored')
        
        return ticker_out, price_out, time_out
        
    def read_text_file(self):
        with open("stockslist.txt",'r') as f:
            lines = [line.rstrip() for line in f]
            output = [line for line in lines if line]

        return output
        
    def run(self):
        start_time = time.time()
        print(datetime.datetime.now(), '|Reading ticker info...')
        tickers = self.read_text_file()
        print(datetime.datetime.now(), '|Fetching data...')
        ticker_out, prices, timestamp = self.get_stocks_information(tickers)
        df = pd.DataFrame(data={'ticker':ticker_out, 'prices':prices, 'time':timestamp})

        
        print(datetime.datetime.now(), '|Saving data...')
        df.to_excel("marketPrice.xlsx")
        df.to_csv('marketPrice.txt', sep='\t', index=False)
        duration = time.time() - start_time
        print(datetime.datetime.now(), f'|Completed in {duration} seconds')
        
StockScraper().run()

