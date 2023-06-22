import pandas as pd
import numpy as np
from numpy import nan as NA
df=pd.DataFrame([[1,2,3],[4,NA,6],[NA,NA,NA]])
# df[1]=NA


# print(df)


# print(df.dropna(axis=1,how='all'))


print(df.dropna(thresh=3))
print(df.fillna(0))
print(df.fillna(method="ffill",limit=1))
