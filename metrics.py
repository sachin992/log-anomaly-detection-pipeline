import pandas as pd

def error_rate(df: pd.DataFrame) -> float:
    """
    Calculate percentage of ERROR logs in the dataset
    """
    total = len(df)
    errors = len(df[df['log_level'] == "ERROR"])
    return (errors / total) * 100 if total else 0.0

def top_endpoints(df: pd.DataFrame, n: int = 5):
    """
    Return the top N most frequently accessed endpoints
    """
    return df['endpoint'].value_counts().head(n)
