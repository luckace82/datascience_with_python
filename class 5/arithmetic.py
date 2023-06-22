import pandas as pd
import numpy as np
s1=pd.Series(np.arange(4),index=["A","b","c","d"])
s2=pd.Series(np.arange(4),index=["q","w","e","r"])
print(s1)
print(s2)
print(s1+s2)
