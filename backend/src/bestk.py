import pybithumb
import numpy as np

class findk:
    def get_ror(k=0.5):
        """
        최근 5일간의 데이터를 통해 k에 대한 수익률을 리턴
        :return: ror
        """
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
        """
        가장 높은 수익률을 기록한 k값을 반환하는 함수
        :return: ret
        """
        max_ror=0
        ret=0
        for k in np.arange(0.1, 1.0, 0.1):
            ror = findk.get_ror(k)
            if max_ror < ror:
                max_ror=ror
                ret=k
        return ret