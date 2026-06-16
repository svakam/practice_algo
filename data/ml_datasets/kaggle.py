import kagglehub
from kagglehub import KaggleDatasetAdapter

# Returns Pandas DataFrames with a specified Kaggle CSV path 

def get_cybersec():
    """
    Returns cybersecurity threat data. 
    (not a great dataset to train on)
    URL: https://www.kaggle.com/datasets/aryanmdev/cybersecurity-threat-dataset-for-malware-detection/data
    """
    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "aryanmdev/cybersecurity-threat-dataset-for-malware-detection",
        "cybersecurity_threat_dataset.csv",
    )
    return df

def get_ai_impact():
    """
    Returns AI impact on students.
    URL: https://www.kaggle.com/datasets/laveshjadon/ai-impact-on-students
    """

    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "laveshjadon/ai-impact-on-students",
        "ai_student_impact_dataset (1).csv",
    )
    return df

