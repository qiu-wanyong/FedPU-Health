import pandas as pd

df = pd.read_csv('Processed_data_Weight_test_true.csv', encoding= 'utf-8') ###
print(df)
vc = df['y'].value_counts()
print(vc)

#df.iloc[0, 1] = 42

pos_sample = df[df["y"] == 1].copy()
pos_sample2 = pos_sample.sample(n=84,random_state=0, axis=0) ###  train:314   test:84
print(pos_sample2)


index = list(pos_sample2.index)
for i in index:
    df.iloc[i, 1] = 0

vc = df['y'].value_counts()
print(vc)
df.to_csv('Processed_data_Weight_test_mask.csv', index=False) ###


# =========================确认过！！样本id是一样的，可以放心探索不同特征====================================
'''
l1 = set(list(df['id']))
df2 = pd.read_csv('Processed_data_totalGain_test_true.csv', encoding= 'utf-8')
l2 = set(list(df2['id']))
print(l1 == l2)
'''
