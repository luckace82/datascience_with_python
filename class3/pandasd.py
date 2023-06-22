import pandas as pd

# dataframe
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
de = pd.Series(data)
print(de)
print(df)
