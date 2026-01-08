import pandas as pd

def detect_anomalies(df: pd.DataFrame):
    """
    Detect traffic spikes using statistical thresholding
    """
    # Count requests per minute
    request_counts = df.groupby(
        df["timestamp"].dt.floor("min")
    ).size()

    # Calculate statistical threshold
    mean = request_counts.mean()
    std = request_counts.std()
    threshold = mean + (2 * std)

    # Identify anomalies
    anomalies = request_counts[request_counts > threshold]
    return anomalies
