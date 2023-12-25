import pandas as pd

df_train = pd.read_csv('Processed_data_Weight_train_mask.csv') ###
df_test = pd.read_csv('Processed_data_Weight_test_mask.csv')   ###
l = list(df_train.columns)
p = 37

fea1 = l[0:p]
fea2 = l[p:]
fea2.insert(0,'id')

df_train_guest = df_train[fea1]
df_train_host = df_train[fea2]

df_test_guest = df_test[fea1]
df_test_host = df_test[fea2]

df_train_guest.to_csv('Processed_data_Weight_train_mask_guest.csv', index=False)  ###
df_train_host.to_csv('Processed_data_Weight_train_mask_host.csv', index=False)    ###

df_test_guest.to_csv('Processed_data_Weight_test_mask_guest.csv', index=False)    ###
df_test_host.to_csv('Processed_data_Weight_test_mask_host.csv', index=False)      ###
