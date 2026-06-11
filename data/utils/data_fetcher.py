from enum import Enum, auto
from data.ml_datasets import uci

class ML(Enum):
    UCI_MAMMO = auto()

def get_data(d: ML):
    match d:
        case d.UCI_MAMMO: return uci.get_mammo()