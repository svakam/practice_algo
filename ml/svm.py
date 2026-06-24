#%% Imports
from sklearn.svm import SVC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%% Get data
# df = pd.read_csv("data/ml_datasets/iris.csv")
df = None
print(df.keys())
# print certain keys to try to get metadata, feature names, etc.

#%% Preprocess
df_feat = pd.DataFrame(df.data, columns=df.feature_names)
print(df_feat.head())