import pandas as pd
ur="https://en.wikipedia.org/wiki/Wikipedia:Fundraising_statistics"
p=pd.read_html(ur)
print(p)