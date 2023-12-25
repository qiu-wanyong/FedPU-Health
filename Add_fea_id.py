import pandas as pd
df = pd.read_csv('feature_importance_all_2.csv', encoding= 'utf-8')
ids = pd.read_csv('feature-a0001wav.csv', encoding= 'utf-8')
ids['key'] = [i for i in range(6373)]
ids.columns = ['Feature Name'] + ids.columns[1:].tolist()

def split(x):
    return x[12:]

ids['Feature Name'] = ids['Feature Name'].apply(split)
print(ids)
dict_ = ids.set_index('Feature Name').to_dict(orient='dict')['key']

def trans(x):
    return dict_[x]


df['Feature ID'] = df['Feature Name'].apply(trans)
print(df)

df.to_csv('feature_importance_all_3.csv', index=False)


### 手动改

