# Import required modules from different files
from LogGenerator import generate_logs
from parser import parse_log_file
from metrics import error_rate, top_endpoints
from analyzer import detect_anomalies
from visualizations import (
    plot_log_level_distribution,
    plot_top_endpoints,
    plot_requests_over_time,
    plot_anomalies
)

def main():
    # Name of the log file to generate and analyze
    log_file = "large.log"

    # Generate synthetic logs with 1 million entries
    generate_logs(log_file, lines=1000000)

    # Parse the log file into a pandas DataFrame
    df = parse_log_file(log_file)
    print("Log file parsed successfully.")

    # Calculate and display metrics
    print("Calculating Metrics...")
    error_rate_value = error_rate(df)
    print(f"Error Rate: {error_rate_value:.2f}%")

    # Find and display top 5 most accessed endpoints
    top_endpoint = top_endpoints(df, n=5)
    print("Top 5 Endpoints:")
    print(top_endpoint)

    # Detect and display traffic anomalies
    anomalies = detect_anomalies(df)
    print("Anomalies Detected:")
    print(anomalies)
    # Visualizations
    plot_log_level_distribution(df)
    plot_top_endpoints(df, n=5)
    plot_requests_over_time(df)
    plot_anomalies(df, anomalies)

# Entry point of the script
if __name__ == "__main__":
    main()
