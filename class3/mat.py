import matplotlib.pyplot as plt
import pandas as pd

games=pd.read_csv("/home/lakesh/Downloads/vgsalesGlobale.csv")
games.plot()
plt.show()