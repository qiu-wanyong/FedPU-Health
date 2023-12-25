import pandas as pd
df = pd.read_csv('feature_importance_all_2.csv', encoding= 'utf-8') ###


top = 10

SHap = list(df['Feature Name'])

weight = df.sort_values(by='weight', ascending=False)
weight_l = list(weight['Feature Name'])[:top]

total_gain = df.sort_values(by='total_gain', ascending=False)
total_gain_l = list(total_gain['Feature Name'])[:top]



total_cover = df.sort_values(by='total_cover', ascending=False)
total_cover_l = list(total_cover['Feature Name'])[:top]

cover = df.sort_values(by='cover', ascending=False)
cover_l = list(cover['Feature Name'])[:top]

gain = df.sort_values(by='total_cover', ascending=False)
gain_l = list(gain['Feature Name'])[:top]

res = list(set(SHap) & set(total_gain_l) & set(weight_l) & set(total_cover_l) & set(cover_l) & set(gain_l))
res = list(set(SHap) & set(total_gain_l) & set(weight_l))
print(res)

'''
selected_fea = df.loc[:69,['Feature Name']]
print(selected_fea)
# selected_fea.to_csv('SHAP_selected_fea.csv')'''

