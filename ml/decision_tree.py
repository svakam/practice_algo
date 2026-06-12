#%% Imports
from data.utils import data_fetcher
import pandas as pd
import numpy as np
print("Imported")

#%% Fetch UCI data
mammo_data = data_fetcher.get_data(data_fetcher.ML.UCI_MAMMO) # returning as a list; idx 0 = features, idx 1 = targets

#%% Inspect tables
features = mammo_data['features']
targets = mammo_data['targets']
combined = pd.concat([features, targets], axis=1) # stack by columns
print(combined.describe())
print(combined.head())

#%% Prepare data
# conv '?' to NaN
# drop missing vals
combined.replace('?', np.nan)
combined.dropna(inplace=True)
combined.describe()

# split into features and targets
features = combined[['Age', 'Shape', 'Margin', 'Density']]
print(features.describe())

targets = combined['Severity']
print(targets.describe())
print(targets.head())

#%% Normalize features via standard-normal
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier

# convert to numpy for scikit-learn
features_np = features.values
targets_np = targets.values
feature_names = ['Age', 'Shape', 'Margin', 'Density']

features_scaled = StandardScaler().fit_transform(features_np)
features_scaled

#%% Operate classifier on one train/test split
# create .25 split
(training_inputs,
 testing_inputs,
 training_targets,
 testing_targets) = train_test_split(features_scaled, targets_np, test_size=0.25, random_state=1)

# initialize classifier and fit on training
clf = DecisionTreeClassifier(random_state=1, max_depth=3, criterion='entropy')
clf.fit(training_inputs, training_targets)

# visualize and score
from IPython.display import Image
from six import StringIO
from sklearn import tree
from pydotplus import graph_from_dot_data

clf.score(testing_inputs, testing_targets)

dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data, feature_names=feature_names)
graph = graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())

#%% Run classifier again on k-fold cross val with hyperparameter experimentation
print("\nTuning hyperparameters with k = 5 fold cross validation...")
from sklearn.model_selection import cross_val_score

clf = DecisionTreeClassifier(random_state=10, max_depth=3, criterion='entropy')

cv_scores = cross_val_score(clf, features_np, targets_np, cv=5)
print(f"5-fold cross validation scores: {cv_scores}")
print(f"Average: {cv_scores.mean()}")

best_max_depth = 1
best_score = 0.0


for i in range(1, 11):
    print(f"max depth: {i}")
    clf = DecisionTreeClassifier(random_state=10, max_depth=i, criterion='entropy')

    cv_scores = cross_val_score(clf, features_np, targets_np, cv=5)
    # print(f"5-fold cross validation scores: {cv_scores}")
    mean = cv_scores.mean()
    print(f"Averages score: {mean}")
    curr_depth = i
    curr_score = mean

    if curr_score > best_score:
        best_score = curr_score
        best_max_depth = curr_depth

    print("\n")

print(f"optimal max_depth: {best_max_depth} with 5-fold cross-val score {best_score}")

