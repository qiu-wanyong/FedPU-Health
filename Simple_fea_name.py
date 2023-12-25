import pandas as pd
df = pd.read_csv('feature_importance_all.csv', encoding= 'utf-8')
def split(x):
    return x[12:]

df['Feature Name'] = df['Feature Name'].apply(split)


df.to_csv('feature_importance_all_2.csv',index=False)