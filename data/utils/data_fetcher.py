from enum import Enum, auto
from data.ml_datasets import uci, kaggle

"""
Whenever adding a new dataset to try to import,
1) add a new enum with <Source>_<Dataset_Name>
2) add a match-case in get_data with new enum and return <module>.<method>()
(method name should be identical or very close to enum name for simplicity)
"""

class ML(Enum):
    UCI_MAMMO = auto()
    KAGGLE_CYBERSEC = auto()
    KAGGLE_AI_IMPACT = auto()

def get_data(d: ML):
    match d:
        case d.UCI_MAMMO: return uci.get_mammo()
        case d.KAGGLE_CYBERSEC: return kaggle.get_cybersec()
        case d.KAGGLE_AI_IMPACT: return kaggle.get_ai_impact()
    return None

# potential to overload with other dataset types