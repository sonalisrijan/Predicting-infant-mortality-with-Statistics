# Python code to remove outlier cases. This code:
# >> Removes missing values from each of the following continuous variables: 'cig_0', 'cig_1', 'cig_2', 'cig_3', 'previs', 'wtgain', 'rf_cesarn'
# >> Removes all observations with cigarettes>=50 (cig_0, cig_1, cig_2, cig_3)
# >> Removes previs>=50
# >> For priorlive, priordead, priorterm: removes data points with >15 in any of these columns
# >> Drops columns iliven, n, lwtgain, lCIG_0, lCIG_1, lCIG_2, lCIG_3
# >> Saves the cleaned training set data as: 1_new_train.csv --


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./1_train.csv", sep=",")
print (data.shape)
train = data.dropna(subset=['cig_0', 'cig_1', 'cig_2', 'cig_3', 'previs', 'wtgain', 'rf_cesarn']) 

# # Check distributions using histograms
# plt.hist(train['cig_0'], bins=20)
# plt.hist(train['cig_1'], bins=20)
# plt.hist(train['cig_2'], bins=20)
# plt.hist(train['cig_3'], bins=20)
# plt.hist(train['previs'], bins=20)
# plt.hist(train['priorterm'], bins=20)
# plt.hist(train['priorlive'], bins=20)
# plt.hist(train['priordead'], bins=20)

train.drop(train[train['cig_0'] > 50].index, inplace = True)
train.drop(train[train['cig_1'] > 50].index, inplace = True)
train.drop(train[train['cig_2'] > 50].index, inplace = True)
train.drop(train[train['cig_3'] > 50].index, inplace = True)
train.drop(train[train['previs'] > 50].index, inplace = True)
train.drop(train[train['priorterm'] > 15].index, inplace = True)
train.drop(train[train['priorlive'] > 15].index, inplace = True)
train.drop(train[train['priordead'] > 15].index, inplace = True)

train.drop(['ilive_n', 'n', 'lwtgain', 'lCIG_0', 'lCIG_1', 'lCIG_2', 'lCIG_3'], axis=1,  inplace=True)

print (train.shape)
train.to_csv("1_new_train.csv", sep=",", index=False)