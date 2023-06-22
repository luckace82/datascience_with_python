import pandas as pd
import numpy as np
df=pd.DataFrame(np.arange(6).reshape(2,3),index=["tim","tom"],columns=list("abc"))
df2=pd.DataFrame(np.arange(9).reshape(3,3),index=["tim","kate","tom"],columns=list("acd"))
print(df)
print(df2)
print(df+df2)
print(df.add(df2,fill_value=0))