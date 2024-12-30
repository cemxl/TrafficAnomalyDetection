import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load the raw traffic data
data = pd.read_csv('traffic_data.csv')

# Select features for anomaly detection
features = data[['time', 'x', 'y', 'speed']]

# Normalize the features
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(features)

# Convert back to a DataFrame
normalized_df = pd.DataFrame(normalized_data, columns=['time', 'x', 'y', 'speed'])

# Save the normalized data to a CSV file
normalized_df.to_csv('normalized_traffic_data.csv', index=False)

print("Normalized data has been saved to 'normalized_traffic_data.csv'.")
