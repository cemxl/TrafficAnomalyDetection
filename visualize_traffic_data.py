import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
data = pd.read_csv('traffic_data.csv')

# Step 2: Plot vehicle speeds over time
for vehicle_id in data['vehicle_id'].unique():
    vehicle_data = data[data['vehicle_id'] == vehicle_id]
    plt.plot(vehicle_data['time'], vehicle_data['speed'], label=vehicle_id)

# Step 3: Add plot details
plt.title('Vehicle Speeds Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')
plt.legend(loc='upper right')
plt.show()
