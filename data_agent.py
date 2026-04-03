import pandas as pd

def load_jobs():
    df = pd.read_csv("data/jobs.csv")
    return df