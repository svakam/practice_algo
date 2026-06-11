from enum import Enum, auto
import ml_datasets

class ML(Enum):
    UCI_MAMMO = auto()

def get_data(d: ML):
    match d:
        case d.UCI_MAMMO: return ml_datasets.uci.get_mammo()