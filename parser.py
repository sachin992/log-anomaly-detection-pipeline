import pandas as pd

def parse_log_file(filepath: str) -> pd.DataFrame:
    """
    Parse raw log file into a structured pandas DataFrame
    """
    columns = ['timestamp', 'log_level', 'endpoint', 'status_code', 'ip_address']

    df = pd.read_csv(
        filepath,
        sep=" ",
        names=columns,
        parse_dates=["timestamp"],
        on_bad_lines="skip"
    )
    return df
