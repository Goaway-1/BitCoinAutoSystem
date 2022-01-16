import pyupbit
import numpy as np

mostKVal = 0
mostK = 0

def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-ETH", count=7)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'],
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    if(mostKVal < ror) : 
        mostKVal = ror 
        mostK = k
    print("%.1f %f" % (k, ror))

mostK = round(mostK,1)
print("mostK %f" % mostK)