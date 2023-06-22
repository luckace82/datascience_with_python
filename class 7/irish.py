import pandas as pd 
import numpy as np 
from numpy import nan as NA


df =pd.DataFrame([[2,4,np.nan],[6.3,-5,4]],index=['a','b','c'],columns=["one","two"])
print(df)