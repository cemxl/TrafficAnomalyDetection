import plotly.express as px
import pandas as pd

# Load traffic data
data = pd.read_csv('traffic_data.csv')

# Add anomaly markers
data['anomaly'] = (data['speed'] > 20) | (data['speed'] < 1)

# Create an interactive scatter plot
fig = px.scatter(
    data,
    x='time',
    y='speed',
    color='anomaly',
    hover_data=['vehicle_id', 'x', 'y'],
    title='Vehicle Speeds Over Time',
    labels={'anomaly': 'Is Anomaly'}
)

# Show the plot
fig.show()
