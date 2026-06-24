#%% Imports
from data.utils import data_fetcher
import pandas as pd
import numpy as np
print("Imported")

#%% Get data
df = None

#%% Inspect

#%% Prepare/pre-process


#%% Train/test split
X_train = None
y_train = None

#%% Fit
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(C=100, solver='liblinear')
model.fit()

#%% Score/predict

#%% Pickle: write/read model and run inference


