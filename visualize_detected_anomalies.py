import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset with anomalies
data = pd.read_csv('traffic_data_with_anomalies.csv')

# Plot anomalies
anomalies = data[data['anomaly'] == True]

plt.scatter(anomalies['time'], anomalies['speed'], color='red', label='Anomalies')
plt.title('Vehicle Speeds with Anomalies')
plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')
plt.legend()
plt.show()
