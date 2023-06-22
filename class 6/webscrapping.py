import numpy as np
import pandas as pd
from bs4 import BeautifulSoup## library for html and xml documents to extract the data
import requests#library used to send htp requests and handle response time in python
import html5lib
url="http://espn.go.com/nfl/superbowl/history/winners"
page=requests.get(url)
soup=BeautifulSoup(page._content,"html.parser")
print(soup)
sb_table=soup.find('table')
print(sb_table)
sb=pd.read_html(str(sb_table))[0]
print(sb.head())