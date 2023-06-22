import pandas as pd
import numpy as np


df=pd.DataFrame(np.random.randn(4,3),index=["KIM","susan","lakesJ","lol"],columns=list("abc"))
# print(df)
def cal(x):
    return x.max()-x.min()
df.apply(cal)
