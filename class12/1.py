import numpy as np
import pandas as pd
from datetime import datetime
date=[datetime(2020,1,5),datetime(2029,1,5),datetime(2020,8,5),datetime(2020,5,5),datetime(2020,3,5)]
print(date)

ts=pd.Series(np.random.randn(5),index=date)
print(ts)


print(pd.to_datetime("01/01/2020"))


dates=pd.to_datetime([datetime(2020,7,5),"th of jul 2020","2020 jul 7","sasa"])
print(dates)
print(dates.to_period("D"))
