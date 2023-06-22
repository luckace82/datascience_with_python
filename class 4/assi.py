import pandas as pd
import numpy as np
# s=pd.Series([1,2,3,4],index=["A","B","C","D"])
# print(s)
 #reindex


# s3=pd.Series(["blue","red","green"],index=[0,2,4])
# #Ffil=forwad fillchoose the nearest value
# print(s3.reindex(range(6),method="ffill"))


df=pd.DataFrame(np.arange(9).reshape(3,3),index=['a','b','c'],columns=[7,8,9])
# print(df)

# df2=df.reindex(index=['d','c','b','a'])
# print(df2)

df2=df.reindex(columns=["tim","otm","kate"])
print(df2)
print(df.loc[["b","c","a"]])