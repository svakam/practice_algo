#%% Imports
from data.utils import data_fetcher
import pandas as pd
import numpy as np
print("Imported")

#%% Fetch Kaggle Cybersecurity Threat data 
# https://www.kaggle.com/datasets/aryanmdev/cybersecurity-threat-dataset-for-malware-detection/data
df = data_fetcher.get_data(data_fetcher.ML.KAGGLE_CYBERSEC)
df
#%% Inspect
print(f"Describe:\n{df.describe()}")
print(f"\nHead:\n{df.head()}")

# for each column, list 
# %%
