# Yahoo Stocks scraper
This is a simple script that scrapes a list of stocks on yahoo and exports them to and excel file.

## Installation and prerequisites
- Python: 3.7-3.10

You can install the required packages using PyPI
``` 
pip3 install -r requirements.txt
```

## Run
First ensure the desired stocks are added to the `stocks.txt` file. Currently there is no support for ETFs and Indexes.

```
python3 main.py
```
The resulting excel file, `output.xlsx`, will contain basic information of each stock.  

