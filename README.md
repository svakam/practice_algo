# Practice Algorithms

A simple, bear-bones repo for algo practice and testing. Problems and helper structures written in C++ or Python (hopefully Rust someday). 

Potential to include CMake to help with GoogleTest integration in the future. 

Python only: can import from external datasets to test against ML algorithms via `import data.utils.data_fetcher`. 

## Setup
Once cloned, run `pip install -e .` to set up packages/module references. Also ensure `ipykernel` is installed to run the code cell-wise. 

## Data
### ML Dataset Sources
- UC Irvine
- Kaggle (Must be authenticated; see `https://www.kaggle.com/settings/api`)

Note: APIs are abstracted into method calls via a 'data fetcher' layer.

```
from data.utils import data_fetcher
import pandas as pd
import numpy as np
print("Imported")
```

## Libraries
### Leetcode

### Other
#### Linear Algebra
- Determinant
- Moving Average
- Gaussian Elimination

#### Machine Learning
- Decision Tree
- K-nearest Neighbors
- Random Forest, Confusion Matrix + Accuracy
- SVM, Gridsearch
- Logistic Regression
