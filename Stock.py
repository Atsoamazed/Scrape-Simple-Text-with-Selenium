import requests
from datetime import datetime
import time

symbol = input("Enter the symbol: ")
from_date = input("Enter the from date yyyy/mm/dd: ")
from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
from_eoch = int(time.mktime(from_datetime.timetuple()))

to_date = input("Enter the to date yyyy/mm/dd: ")
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')
to_eoch = int(time.mktime(to_datetime.timetuple()))

url= f"https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={from_eoch}&period2={to_eoch}&interval=1mo&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

content = requests.get(url, headers=headers).content
print(content)

with open('aapl.csv', 'wb') as file:
  file.write(content)
  print("done")
