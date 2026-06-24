#%% Imports
from data.utils import data_fetcher
import pandas as pd
import numpy as np
print("Imported")

#%% Fetch data
df = data_fetcher.get_data(data_fetcher.ML.KAGGLE_AI_IMPACT)

#%% Inspect

print(f"Inspecting data...\nDescribe:\n{df.describe()}")
print(f"\nHead:\n{df.head()}\n")

# for each column, list unique values
for i, col in enumerate(df.columns):
    print(i, col)

print(f"\n{df.dtypes}")

print(f"\nPerceived AI dependency scale: {df['Perceived_AI_Dependency'].min()} to {df['Perceived_AI_Dependency'].max()}")
print(f"\nAnxiety level scale: {df['Anxiety_Level_During_Exams'].min()} to {df['Anxiety_Level_During_Exams'].max()}")
#%% Preprocess

null_df = df.isnull().sum()
print(f"\n# NaN's: {null_df.values.sum()}")
if (null_df.values.sum() > 0):
    print("\nDropping NaNs...")
    df.dropna(inplace=True)
else:
    print("\nNo NaN's found")

df.describe()
#%% Extract features and targets
"""
Question: how is burnout risk level affected by features:
- Pre-semester GPA (float64)
- Weekly GenAI Hours (float64)
- Perceived AI Dependency (int64, 1-10)
- Anxiety Level During Exams (int64, 1-10)
- Paid Subscription (bool)
- Prompt Engineering Skill (str)
""" 
targets = df[['Burnout_Risk_Level']]
features = df[['Pre_Semester_GPA', 'Weekly_GenAI_Hours', 'Perceived_AI_Dependency', \
               'Anxiety_Level_During_Exams', 'Paid_Subscription', 'Prompt_Engineering_Skill']]

print(len(features) == len(targets))
#%% Normalization
from sklearn.preprocessing import StandardScaler, LabelEncoder

# convert categorical to numerical
print("\nConverting categorical values to numerical...")

p = 'Prompt_Engineering_Skill'
b = 'Burnout_Risk_Level'
print(f"for {p}\n")
print(features[p].head())

labelencoder_feat = LabelEncoder()
features[p] = labelencoder_feat.fit_transform(features[p])
print(features[p].head())

print(f"for {b}\n")
print(targets[b].head())

labelencoder_target = LabelEncoder()
targets[b] = labelencoder_target.fit_transform(targets[b])
print(targets[b].head())

features_np = features.values
targets_np = targets.values.ravel()

features_scaled = StandardScaler().fit_transform(features_np)
features_scaled

#%% Classify and score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

(training_inputs, 
 testing_inputs, 
 training_targets, 
 testing_targets) = train_test_split(features_scaled, targets_np, test_size=0.25, random_state=1)

# set up classifier and train it on training data (inputs, targets)
clf = RandomForestClassifier(n_estimators=50, criterion='gini', random_state=1, n_jobs=-1)
clf.fit(training_inputs, training_targets)

# run the classifier on test inputs and output predicted targets
predicted_targets = clf.predict(testing_inputs)

# confusion matrix and accuracy score to compare testing targets to predicted
cm = confusion_matrix(testing_targets, predicted_targets)
print(cm)

score = accuracy_score(testing_targets, predicted_targets)
print(score)

acc_threshold = 0.8

#%% If accuracy score below threshold, try boosting and XGBoosting
from sklearn.ensemble import GradientBoostingClassifier
import xgboost as xgb
import matplotlib.pyplot as plt
if (score < acc_threshold):
    GBC = GradientBoostingClassifier()
    GBC.fit(training_inputs, training_targets)
    y_pred = GBC.predict(testing_inputs)
    boosted_score = GBC.score(testing_inputs, testing_targets)
    print(boosted_score)

    print(f"Score gradient-boosted by {(boosted_score - score):.5f}")

    if (boosted_score < acc_threshold):
        XGBC = xgb.XGBClassifier()
        XGBC.fit(training_inputs, training_targets)
        xgb_pred = XGBC.predict(testing_inputs)
        xgb_score = XGBC.score(testing_inputs, testing_targets)
        print(xgb_score)

        print(f"Score XG-boosted by {(xgb_score - score):.5f}")
        print(f"XG-Boost improves upon gradient boosting by {(xgb_score - boosted_score):.5f}")

        xgb.plot_importance(XGBC) # how do I label these cols
        plt.rcParams['figure.figsize'] = [5,5]
        plt.show()


