import pandas as pd
import datetime
from forex_python.converter import get_rate

day1 = datetime.date(2022, 5, 1)
currency = []
while True:
    currency.append(get_rate("EUR", "PLN", day1))
    day1 = day1 + datetime.timedelta(days = 1)
    if day1 == datetime.date(2022, 5, 15)+datetime.timedelta(days = 1):
        break
t = pd.date_range(start="2022-05-01",end=datetime.date(2022, 5, 15))
USDtoPLN = pd.Series(data=currency, index=t)
print (USDtoPLN)

