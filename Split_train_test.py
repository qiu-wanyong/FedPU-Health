import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('Processed_data_Weight.csv', encoding= 'utf-8') ###
X = df.iloc[:,2:]
y = df['y']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

df1 = pd.concat([y_train, X_train], axis=1)
df1.index.name = 'id'
df2 = pd.concat([y_test, X_test], axis=1)
df2.index.name = 'id'

df1.to_csv('Processed_data_Weight_train_true.csv', index=True) ###
df2.to_csv('Processed_data_Weight_test_true.csv', index=True)  ###