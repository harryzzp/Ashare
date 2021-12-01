from Ashare import *
from MyTT import *
import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick2_ochl
from mplfinance.original_flavor import volume_overlay
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# http://hq.sinajs.cn/list=sz002307,sh600928
# https://ifzq.gtimg.cn/appstock/app/kline/mkline?param=sh600519,m15,,16
data = get_price('000001.XSHG', frequency='1m', count=120)  # 默认获取今天往前120天的日线行情
print('行情\n', data.head(10))
TIME = pd.to_datetime(data.index.values)

fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(17, 12))

candlestick2_ochl(ax, data['open'], data['close'], data['high'],
                  data['low'], width=0.5, colorup='r', colordown='g', alpha=0.6)

CLOSE = data.close.values
MA5 = MA(CLOSE, 5)
MA10 = MA(CLOSE, 10)
up,mid,lower=BOLL(CLOSE) 

ax.plot(MA5, label='5 MA',linewidth=0.5,alpha=0.7)
ax.plot(MA10, label='10 MA',linewidth=0.5,alpha=0.7)
ax.plot(up,label='UP');
ax.plot(mid,label='MID');
ax.plot(lower,label='LOW');
ax.grid(True)
ax.legend(loc='upper left')
xtick = range(0, len(TIME))
plt.xticks(xtick, TIME)

plt.grid(0)
# plt.title('上证指数', fontsize=10)
plt.title('上证指数')

# data['volume'].plot(kind='bar', color='k', alpha=0.3, label='Volume')
volume_overlay(ax2, data['open'], data['close'], data['volume'], colorup='r', colordown='g', width=0.5, alpha=0.8)
ax2.set_xticks(xtick, 10)
ax2.set_xticklabels(TIME)
ax2.grid(True)
# ax2.yaxis.set_label_position("right")
# ax2.set_ylabel('Volume', size=20)
ax2.set_ylabel('Volume')

plt.gcf().autofmt_xdate(rotation=45)
plt.subplots_adjust(hspace=0)

plt.show()
