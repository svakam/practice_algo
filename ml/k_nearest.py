#%% Imports
from data.utils import data_fetcher
import pandas as pd
import numpy as np
print("Imported")

#%% Preprocess UCI data
print("\nPreprocessing...")
mammo_data = data_fetcher.get_data(data_fetcher.ML.UCI_MAMMO) # returning as a list; idx 0 = features, idx 1 = targets
features = mammo_data['features']
targets = mammo_data['targets']
combined = pd.concat([features, targets], axis=1)
combined.replace('?', np.nan)
combined.dropna(inplace=True)


#%% Split into features and targets
print("\nSplitting features and targets...")
features = combined[['Age', 'Shape', 'Margin', 'Density']]
targets = combined['Severity']
print(features, targets)

#%% Normalize features
print("\nNormalizing features...")
from sklearn.preprocessing import StandardScaler

# convert to numpy
features_np = features.values
targets_np = targets.values

features_scaled = StandardScaler().fit_transform(features_np)
features_scaled

#%% Run k-neighbors and tune hyperparameters
print("Running 10-fold cross validation on k-neighbors and tuning hyperparameters...")
from sklearn import neighbors
from sklearn.model_selection import cross_val_score

best_score = 0.0
best_k = 1

for i in range(1, 15):
    clf = neighbors.KNeighborsClassifier(n_neighbors=i)
    cv_scores = cross_val_score(clf, features_scaled, targets_np, cv=10)
    
    curr_neighbors = i
    curr_score = cv_scores.mean()
    print(f"\n{i} neighbors scored {curr_score}")

    if (curr_score > best_score):
        best_score = curr_score
        best_k = i

print(f"Found optimal k to be {best_k} with score {best_score}.")

# %%
