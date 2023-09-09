import pandas as pd

data = pd.read_excel("lab_pi_101.xlsx")
#idx = pd.Index(data)
#idx.unique()
#idx.count = ()
#print(idx.value_counts)
data = data.drop_duplicates (subset=['col1', 'col2'])
print(data)