import pandas as pd

# url="https://raw.githubusercontent.com/fivethirtyeight/data/master/unisex-names/unisex_names_table.csv"
# name=pd.read_csv(url)
# print (name)
# # ptint(name.head())
# # name=name.drop(columns="unnamed:0")


url2="https://raw.githubusercontent.com/fivethirtyeight/data/master/classic-rock/classic-rock-song-list.csv"
rock=pd.read_csv(url2)
print(rock)