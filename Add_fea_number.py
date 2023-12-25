import pandas as pd
df = pd.read_csv('feature_importance_all_3.csv', encoding= 'utf-8')
print(df)
df.to_csv('feature_importance_all_4.csv', index=True)