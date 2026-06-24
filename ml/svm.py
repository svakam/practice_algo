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
df_target = pd.DataFrame(df.target, columns=[""])
df_target.head()

#%% Fit
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

X_train, X_test, y_train, y_test = train_test_split(df_feat, df_target, test_size=0.30, random_state=101)

model = SVC(C=1, gamma=0.01)
model.fit(X_train, y_train)

#%% Score & Predict
from sklearn.metrics import classification_report, confusion_matrix
score = model.score(X_test, y_test)
print(f"Model Accuracy: {score}")

predictions = model.predict(X_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))   

#%% Grid search for hyperparameter tuning + refitting
from sklearn.model_selection import GridSearchCV

param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001], 'kernel': ['rbf', 'linear']}

# args: SVC instance, param grid, then optional
grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2)
grid.fit(X_train, y_train)

print("Best params:", grid.best_params_)
print("Best estimator:", grid.best_estimator_)

#%% Predict with best estimator and score
grid_predictions = grid.predict(X_test)

grid.score(X_test, y_test)

print("Confusion matrix:", confusion_matrix(y_test, grid_predictions))
print("Classification report:", classification_report(y_test, grid_predictions))

