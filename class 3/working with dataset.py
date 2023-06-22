import pandas as pd
games=pd.read_csv("/home/lakesh/Downloads/vgsalesGlobale.csv")
# print(games.head(10))


# print(games.dtypes)#it gives us datatypes


# print(games.Genre.describe())#descriptivesattistics
# print(games.Genre.value_counts())#descriptivesattistics


#realtive fquency

# print(games.Genre.value_counts(normalize=True))



# #edtermine the data type
# genre_counts = games.Genre.value_counts()
# print(type(genre_counts))



# #generate unipue values
# print(games.Genre.unique())



#contingency table or cross tabulation
print(pd.crosstab(games.Genre, games.Global_Sales))
print(games.Global_sales.mean())

