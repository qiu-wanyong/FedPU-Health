import pandas as pd
a = pd.read_csv('XG_feature.csv', encoding= 'utf-8')
b = pd.read_csv('Shap_feature.csv', encoding= 'utf-8')
a.columns = ['feature_name'] + a.columns[1:].tolist()
b.columns = ['feature_name'] + b.columns[1:].tolist()
b2 = b[b['Shap value']>0]

'''
seta = set(list(a['feature_name']))
setb = set(list(b2['feature_name']))
print(seta == setb)  # True
'''

weight = a.sort_values(by='weight', ascending=False)
weight_l = list(weight['feature_name'])

total_gain = a.sort_values(by='total_gain', ascending=False)
total_gain_l = list(total_gain['feature_name'])

SHap = list(b2['feature_name'])

total_cover = a.sort_values(by='total_cover', ascending=False)
total_cover_l = list(total_cover['feature_name'])

cover = a.sort_values(by='cover', ascending=False)
cover_l = list(cover['feature_name'])

gain = a.sort_values(by='total_cover', ascending=False)
gain_l = list(gain['feature_name'])

'''
print(weight_l)
print(SHap)
print(total_gain_l)
print(total_cover_l)
print(cover_l)
print(gain_l)
'''

# ========================Feature num analysis==============================
'''
index = []
flags = []
for i in range(len(SHap)):
    flag = 0
    index.append(i)
    w = set(weight_l[:i+1])
    s = set(SHap[:i+1])
    tg = set(total_gain_l[:i+1])
    tc = set(total_cover_l[:i+1])
    c = set(cover_l[:i+1])
    g = set(gain_l[:i+1])

    if(w == s):
        flag = flag + 1
    if(w == tg):
        flag = flag + 1
    if(w == tc):
        flag = flag + 1
    if(w == c):
        flag = flag + 1
    if(w == g):
        flag = flag + 1
    if(s == tg):
        flag = flag + 1
    if(s == tc):
        flag = flag + 1
    if(s == c):
        flag = flag + 1
    if(s == g):
        flag = flag + 1
    if(tg == tc):
        flag = flag + 1
    if(tg == c):
        flag = flag + 1
    if(tg == g):
        flag = flag + 1
    if(tc == c):
        flag = flag + 1
    if(tc == g):
        flag = flag + 1
    if(c == g):
        flag = flag + 1

    flags.append(flag)
'''
'''
d = dict(zip(index, flags))
print(d)
df = pd.DataFrame([d]).T
df.columns = ['Same_Num']
df = df.reset_index().rename(columns={'index':'Slice_index'})
print(df)
df.to_csv('Feature_num_analysis.csv', index=False)
'''
# ==========================================================================

# =========================取70个特征数=======================================
data = pd.read_csv('Merge_sampled.csv', encoding= 'utf-8')

selected_fea = [str(i) for i in weight_l[:70]] #####
selected_fea.insert(0, 'y')
selected_fea.insert(0, 'id')
data_new = data[selected_fea].copy()


def convert_label(x):
    if(x == 0):
        return 1
    if(x == 1):
        return 0

data_new['y'] = data_new['y'].apply(convert_label)
print(data_new)
data_new.to_csv('Processed_data_Weight.csv', index=False) #####
