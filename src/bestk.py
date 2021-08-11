import pybithumb
import numpy as np

class findk:
    def get_ror(k=0.5):
        df = pybithumb.get_ohlcv("BTC")
        df = df.tail() # 최근 5일
        df['range'] = (df['high'] - df['low']) * k
        df['target'] = df['open'] + df['range'].shift(1)

        df['ror'] = np.where(df['high'] > df['target'],
                             df['close'] / df['target'],
                             1)

        ror = df['ror'].cumprod()[-2]
        return ror



    def get_max_ror_k(self):
        max_ror=0
        ret=0
        for k in np.arange(0.1, 1.0, 0.1):
            ror = findk.get_ror(k)
            if max_ror < ror:
                max_ror=ror
                ret=k
        return ret