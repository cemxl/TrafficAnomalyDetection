import xml.etree.ElementTree as ET
import csv

# Load the XML file
try:
    tree = ET.parse('traffic_output.xml')
    root = tree.getroot()

    # Open a CSV file for writing
    with open('traffic_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['time', 'vehicle_id', 'x', 'y', 'speed'])

        # Parse each timestep in the XML file
        for timestep in root.findall('timestep'):
            time = timestep.get('time')
            for vehicle in timestep.findall('vehicle'):
                vehicle_id = vehicle.get('id')
                x = vehicle.get('x')
                y = vehicle.get('y')
                speed = vehicle.get('speed')
                writer.writerow([time, vehicle_id, x, y, speed])

    print("CSV file created successfully: traffic_data.csv")

except FileNotFoundError:
    print("Error: traffic_output.xml not found in the current directory.")
except Exception as e:
    print(f"An error occurred: {e}")
