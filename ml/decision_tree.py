#%% imports
from data.utils import data_fetcher, ML # enum

#%% Fetch UCI data

[features, targets] = data_fetcher.get_data(ML.UCI_MAMMO)
print(features.head)
print(targets.head)

# set up tree

# import UCI mammogramic dataset

# prepare data
# conv question marks to NaN
# add in column names
# set up input values (features) and outputs (classes) by dividing them into separate tables
# normalize dataset (bring all values to a 0-1 standard, i.e. minmax scaling, OR between -3 and 3 i.e. standard normal)
# # applies similarity rules
# # preprocessing.StandardScaler()
# create a single train/test split via sklearn.model_selection.train_test_split(all_features_scaled, all_classes, test_size=<proportion/1 to test on>, random_state=1)
