import pandas as pd
xg = pd.read_csv('XG_feature.csv', encoding= 'utf-8')
xg.columns = ['key'] + xg.columns[1:].tolist()
SHAP = pd.read_csv('Shap_feature.csv', encoding= 'utf-8')
names = pd.read_csv('feature-a0001wav.csv', encoding= 'utf-8')
names['key'] = [i for i in range(6373)]

new = pd.merge(SHAP,names,left_on='Feature name',right_on='key')
new2 = new.loc[new['Shap value'] > 0]
new2 = new2.drop('key',axis=1)

new3 = pd.merge(new2,xg,left_on='Feature name',right_on='key')

new4 = new3.drop(['Feature name', 'key'],axis=1)
#new4.to_csv('feature_importance_all.csv', index=False)

###之后有手动修改
