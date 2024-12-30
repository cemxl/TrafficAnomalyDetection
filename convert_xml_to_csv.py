import xml.etree.ElementTree as ET
import pandas as pd

# Load the XML file
tree = ET.parse('traffic_output.xml')
root = tree.getroot()

# Create an empty list to store data
data = []

# Iterate through the XML to extract relevant data
for vehicle in root.findall('vehicle'):
    vehicle_id = vehicle.get('id')
    time = vehicle.get('time')
    x = vehicle.get('x')
    y = vehicle.get('y')
    speed = vehicle.get('speed')

    # Append data to the list
    data.append([vehicle_id, time, x, y, speed])

# Convert list to a pandas DataFrame
df = pd.DataFrame(data, columns=['Vehicle ID', 'Time', 'X', 'Y', 'Speed'])

# Save to CSV
df.to_csv('traffic_data.csv', index=False)

print("XML data has been successfully converted to traffic_data.csv!")
