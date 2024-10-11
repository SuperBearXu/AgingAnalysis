import pandas as pd

a = {'a': 1,
     'b': 2,
     'c': 3,
     'd': 4}
print(pd.Series(a))

df = pd.Series(a)
df.to_excel('test.xlsx')
