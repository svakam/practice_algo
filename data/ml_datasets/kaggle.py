import kagglehub
from kagglehub import KaggleDatasetAdapter

def get_cybersec():
    # Load a DataFrame with specific CSV
    # https://www.kaggle.com/datasets/aryanmdev/cybersecurity-threat-dataset-for-malware-detection/data
    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "aryanmdev/cybersecurity-threat-dataset-for-malware-detection",
        "cybersecurity_threat_dataset.csv",
    )
    return df