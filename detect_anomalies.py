import pandas as pd

# Load the CSV file
data = pd.read_csv('traffic_data.csv')

# Identify anomalies: Speeds above 20 m/s or below 1 m/s
anomalies = data[(data['speed'] > 20) | (data['speed'] < 1)]

# Save anomalies to a CSV file
anomalies.to_csv('traffic_anomalies.csv', index=False)

# Print some details
print(f"Total anomalies detected: {len(anomalies)}")
print(anomalies.head())
