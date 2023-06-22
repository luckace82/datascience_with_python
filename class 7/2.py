import pandas as pd 
import numpy as np 
from numpy import nan as NA

data=pd.Series([1,0,NA,5])
print(data.fillna(data.mean()))