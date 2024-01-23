import pandas as pd
import numpy as np
long_series = pd.Series(np.random.randn(1000))
# print(long_series.head(2))
# print(long_series.tail(2))
# print(long_series.array)
ser = pd.Series(pd.date_range("2000", periods=2, tz="CET"))
print(ser.to_numpy(dtype=object))
