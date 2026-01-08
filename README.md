# Log Analytics & Anomaly Detection – Data Engineering + ML Project

This project demonstrates an end-to-end data engineering pipeline for large-scale server log analytics. It includes synthetic log generation, parsing, metric computation, anomaly detection, and visualizations, showcasing how raw log data can be transformed into actionable insights using Python.

## 🚀 Project Overview
- Generate large synthetic log files (1M+ records)
- Parse unstructured logs into structured data
- Compute operational metrics (error rate, top endpoints)
- Detect traffic anomalies using statistical techniques
- Visualize request trends and anomalies

## 🧠 Concepts Covered
- Data Engineering (ETL pipeline)
- Log processing & aggregation
- Feature extraction
- Statistical anomaly detection
- Data visualization

## 🛠 Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## 📂 Project Structure
.
├── LogGenerator.py # Generates synthetic log data
├── parser.py # Parses raw log files
├── metrics.py # Computes log metrics
├── analyzer.py # Detects anomalies
├── visualizations.py # Generates plots
├── main.py # Orchestrates the pipeline
├── requirements.txt
└── README.md


## ▶️ How to Run
```bash
pip install -r requirements.txt
python main.py

📊 Output

Error rate percentage

Top requested API endpoints

Time-based anomaly detection

Visual plots of traffic patterns

🎯 Use Case

This project is ideal for learning log analytics, data pipelines, observability systems, and ML-inspired anomaly detection, similar to real-world monitoring systems used in production environments.