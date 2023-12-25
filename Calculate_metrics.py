import pandas as pd
from sklearn.metrics import accuracy_score, recall_score, f1_score

pred_df = pd.read_csv('data(totalCover).csv', encoding= 'utf-8') ###
true_df = pd.read_csv('Processed_data_totalCover_test_true.csv', encoding= 'utf-8') ###
true_df2 = true_df.sort_values(by='id', ascending=True)
df = pd.read_csv('Processed_data_totalCover_test_mask_guest.csv', encoding= 'utf-8') ###
#print(true_df2)
#print(pred_df)
vc3 = df['y'].value_counts()
print(vc3)
vc = pred_df['label'].value_counts()
print(vc)
vc2 = true_df2['y'].value_counts()
print(vc2)



#true = list(pred_df['label'])
true = list(true_df2['y'])
#pred_ = list(pred_df['predict_score'])
#pred = [int(i>=0.2) for i in pred_]
pred = list(pred_df['predict_result'])
print(true)
print(pred)

Acc = accuracy_score(true, pred)
UAR = recall_score(true, pred, average='macro')
UF1 = f1_score(true, pred, average='macro')
print(Acc)
print(UAR)
print(UF1)