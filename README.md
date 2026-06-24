# Practice Algorithms

A simple, bear-bones repo for algo practice and testing. Problems and helper structures written in C++ or Python (hopefully Rust someday). 

I was hoping to include CMake to help with GoogleTest integration, but I'd rather avoid that hassle for the sake of focusing on coding. 

Python only: Can import from external datasets to test against ML algorithms via `import data.utils.data_fetcher`. 

## Setup
Once cloned, run `pip install -e .` to set up packages/module references. Also ensure `ipykernel` is installed to run the code cell-wise. 

## Data
### ML Dataset Sources
- UC Irvine
- Kaggle (MUST be authenticated. See `https://www.kaggle.com/settings/api`)

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

#### Machine Learning
- Decision Tree
- K-nearest Neighbors
- Random Forest, Confusion Matrix + Accuracy
- SVM