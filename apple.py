
# Jupyter Notebook以外で実行する場合は、
# 上の「%matplotlib inline」を削除する
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
#import pandas_datareader as web
import pandas_datareader.data as web

aapl = web.DataReader("AAPL", "google", "2001/12/31", "2016/12/31")["Close"]
aapl.plot() # 株価のプロット