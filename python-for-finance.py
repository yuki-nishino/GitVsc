import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#開始日時と終了日時の指定
# start = dt.datetime(2000,1,1)
# end = dt.datetime(2019,12,31)

# ##yahooから、指定の開始・終了日時のテスラの株価を、変数df(データフレーム)に格納する
# df = web.DataReader('TSLA','yahoo',start,end)

# ##dfの先頭６行を表示する
# print(df.head(6)) 

# ##dfの末尾６行を表示する
# print(df.tail(6))

# ##csv fileに株価を格納する
# df.to_csv('tsla.csv')

##csvに保存した株価をデータフレームdf1に格納する
df1 = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)

df1[['Open','High','Low','Close']].plot()
plt.show()

