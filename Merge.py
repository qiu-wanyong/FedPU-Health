import pandas as pd

a = pd.read_csv('Raw_data/a.csv', encoding= 'utf-8')
b = pd.read_csv('Raw_data/b.csv', encoding= 'utf-8')
c = pd.read_csv('Raw_data/c.csv', encoding= 'utf-8')
d = pd.read_csv('Raw_data/d.csv', encoding= 'utf-8')
e = pd.read_csv('Raw_data/e.csv', encoding= 'utf-8')
f = pd.read_csv('Raw_data/f.csv', encoding= 'utf-8')

merge = pd.concat([a,b,c,d,e,f])
merge2 = merge.drop('id', axis=1)
col = [i for i in range(merge2.shape[0])]
merge2.insert(loc=0, column='id', value=col)
merge2.to_csv('Merge_data.csv', index=False)