import pandas as pd
import numpy as np
# obj=pd.Series(np.arange(5),index=['a','b','c','d','e'])






# obj[1:3]=5
# print(obj)


# data=pd.DataFrame(
#     np.arange(16).reshape(4,4),
#     index=["london","paris","berlin","istanbul"],
#     columns=["one","two","there","four"]
    
# )
# print(data)
# o=data[data["four"]>5]=0
# print(o)
# print(data.iloc["paris"])


toy_data=pd.Series(np.arange(5),index=["a","b","c","d","e"])
print(toy_data)
print(toy_data[-1])