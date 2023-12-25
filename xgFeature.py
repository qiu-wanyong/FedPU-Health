
import pandas as pd
import xgboost as xgb

# 利用xgb.train中的get_score得到weight，gain，以及cover
params={        'max_depth':3,   # 构建树的深度，越大越容易过拟合
                'n_estimators':30,  # 树的个数
                'learning_rate':0.3, # 如同学习率
                'nthread':4,
                'subsample':1.0,  # 随机采样训练样本 训练实例的子采样比
                'colsample_bytree':1, # 生成树时进行的列采样
                'min_child_weight' : 3, # 这个参数默认是 1，是每个叶子里面 h 的和至少是多少，对正负样本不均衡时的 0-1 分类而言
                                        #，假设 h 在 0.01 附近，min_child_weight 为 1 意味着叶子节点中最少需要包含 100 个样本。
                                        # 这个参数非常影响结果，控制叶子节点中二阶导的和的最小值，该参数值越小，越容易 overfitting。
                'seed':1301} # 随机种子

train = pd.read_csv('Merge_sampled.csv', encoding= 'utf-8')
val = pd.read_csv('./Raw_data/validate.csv', encoding= 'utf-8')

train_y, val_y = train['y'], val['y']
train_X, val_X = train.iloc[:,2:], val.iloc[:,2:]

xgtrain = xgb.DMatrix(train_X, label=train_y)
xgval = xgb.DMatrix(train_X, label=train_y)

# bst = xgb.train(params, xgtrain, num_boost_round=50)
model = xgb.train(params,
          dtrain=xgtrain,
          verbose_eval=True,
          evals=[(xgtrain, "train"), (xgval, "valid")],
          early_stopping_rounds=10,
          num_boost_round = 30
                  )

# ***************自定义特征重要性指标***************
# 'weight', 'gain', 'cover', 'total_gain', 'total_cover'
# 在所有树中，某特征被⽤来分裂节点的次数
# 表⽰在所有树中，某特征在每次分裂节点时处理(覆盖)的所有样例的数量
# cover = total_cover / weight
# 在所有树中，某特征在每次分裂节点时带来的总增益
# gain = total_gain / weight
# 在平时的使⽤中，多⽤total_gain来对特征重要性进⾏排序
importance_eval_list = ['weight', 'gain', 'cover', 'total_gain', 'total_cover']
for i, importance_type in enumerate(importance_eval_list):
    feat_importance = model.get_score(importance_type=importance_type)
    feat_importance = pd.DataFrame.from_dict(feat_importance, orient='index')
    feat_importance.columns = [importance_type]
    if i == 0:
        df_temp = feat_importance
    else:
        df_temp = pd.merge(df_temp, feat_importance, how='outer', left_index=True, right_index=True)
        print('%s: ' % importance_type, model.get_score(importance_type=importance_type))

print('特征重要性结果为:\n', df_temp)

feat_importance_name = 'XG_feature.csv'

df_temp.to_csv(feat_importance_name, index=True)




