import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style="whitegrid")


def plot_log_level_distribution(df: pd.DataFrame):
    """
    Plot distribution of log levels (INFO, ERROR, etc.)
    """
    plt.figure(figsize=(8, 5))
    sns.countplot(x="log_level", data=df)
    plt.title("Log Level Distribution")
    plt.xlabel("Log Level")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


def plot_top_endpoints(df: pd.DataFrame, n: int = 5):
    """
    Plot top N most accessed endpoints
    """
    top_eps = df["endpoint"].value_counts().head(n)

    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_eps.index, y=top_eps.values)
    plt.title(f"Top {n} Endpoints")
    plt.xlabel("Endpoint")
    plt.ylabel("Request Count")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


def plot_requests_over_time(df: pd.DataFrame):
    """
    Plot requests per minute (time series)
    """
    req_per_min = df.groupby(
        df["timestamp"].dt.floor("min")
    ).size()

    plt.figure(figsize=(12, 5))
    req_per_min.plot()
    plt.title("Requests Per Minute")
    plt.xlabel("Time")
    plt.ylabel("Request Count")
    plt.tight_layout()
    plt.show()


def plot_anomalies(df: pd.DataFrame, anomalies: pd.Series):
    """
    Plot traffic with anomalies highlighted
    """
    req_per_min = df.groupby(
        df["timestamp"].dt.floor("min")
    ).size()

    plt.figure(figsize=(12, 5))
    plt.plot(req_per_min.index, req_per_min.values, label="Normal Traffic")
    plt.scatter(
        anomalies.index,
        anomalies.values,
        color="red",
        label="Anomalies"
    )

    plt.title("Traffic Anomaly Detection")
    plt.xlabel("Time")
    plt.ylabel("Request Count")
    plt.legend()
    plt.tight_layout()
    plt.show()
