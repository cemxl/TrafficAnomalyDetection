# TrafficAnomalyDetection
A traffic simulation and anomaly detection framework using SUMO and Python.
Overview
This project is a proof of concept for simulating traffic and detecting anomalies in vehicle behavior, inspired by the research paper:
"Deep Learning-Based Anomaly Detection for Fog-Assisted IoVs Networks."

The project uses:

SUMO (Simulation of Urban Mobility) for traffic simulation.
Python for data processing, visualization, and machine learning-based anomaly detection.
The framework identifies irregular vehicle behaviors (e.g., speeding, halting) using both rule-based methods and deep learning techniques, laying the groundwork for smarter traffic management systems.

Objectives
Simulate realistic traffic patterns and generate vehicle behavior data.
Detect anomalies in traffic behavior:
Rule-based: Speeds exceeding or dropping below thresholds.
Machine learning: An autoencoder to flag subtle anomalies.
Visualize traffic patterns and anomalies dynamically.
Features
Traffic Simulation:

Simulates traffic on a custom road network with junctions, edges, and traffic lights.
Outputs vehicle behavior data (e.g., speed, position, time).
Anomaly Detection:

Rule-Based Detection: Detects anomalies based on thresholds.
Machine Learning Detection: Uses an autoencoder for more nuanced anomaly detection.
Visualizations:

Interactive graphs for analyzing traffic patterns and anomalies.
Real-time simulation visualization in SUMO-GUI.
Project Workflow
Traffic Simulation:

Create and configure a road network in SUMO using NetEdit.
Define vehicle routes and simulate traffic behavior.
Data Collection:

Extract vehicle behavior data (speed, position, time) from SUMO simulations.
Convert XML outputs to CSV for easier processing.
Anomaly Detection:

Apply rule-based thresholds for quick anomaly identification.
Train an autoencoder to learn normal traffic patterns and flag anomalies based on reconstruction errors.
Visualization:

Generate graphs to analyze speed, anomalies, and traffic trends.
Visualize real-time simulations in SUMO-GUI.
Installation
Prerequisites
Python 3.12 (or a similar version)
SUMO (Simulation of Urban Mobility):
Download SUMO and install it.
Add SUMO's bin directory to your system PATH.
Required Python libraries:
Install dependencies using:
bash
Copy code
pip install pandas numpy matplotlib tensorflow plotly
Setting Up
Clone the repository:

bash
Copy code
git clone https://github.com/YourUsername/TrafficAnomalyDetection.git
cd TrafficAnomalyDetection
Verify SUMO installation:

bash
Copy code
sumo --version
Ensure xml2csv.py (from SUMO tools) is accessible:

bash
Copy code
python "C:/Program Files/Eclipse/Sumo/tools/xml/xml2csv.py" --help
How to Run the Project
1. Traffic Simulation
Open your network file in NetEdit:

bash
Copy code
netedit
Design or load a road network (e.g., TrafficAnomalyProject.net.xml).

Define traffic routes and save the configuration (simulation.sumocfg).

Run the simulation in SUMO-GUI:

bash
Copy code
sumo-gui -c simulation.sumocfg
2. Data Collection
Convert SUMO’s XML output (traffic_output.xml) to CSV:

bash
Copy code
python "C:/Program Files/Eclipse/Sumo/tools/xml/xml2csv.py" traffic_output.xml -o traffic_data.csv
The output file traffic_data.csv will contain vehicle information.

3. Anomaly Detection
Rule-Based Detection:
Run the rule-based detection script:

bash
Copy code
python detect_anomalies_rule_based.py
Output: traffic_anomalies.csv with flagged anomalies.

ML-Based Detection:
Train an autoencoder and detect anomalies:

bash
Copy code
python detect_anomalies_ml.py
Output: Anomalies identified using reconstruction errors.

4. Visualizations
Run the visualization script to generate interactive graphs:

bash
Copy code
python visualize_traffic_data.py

File Structure

TrafficAnomalyProject/
├── .gitignore

├── traffic_output.xml       # SUMO simulation output

├── traffic_data.csv         # Processed traffic data

├── traffic_anomalies.csv    # Detected anomalies

├── detect_anomalies_rule_based.py   # Rule-based anomaly detection

├── detect_anomalies_ml.py           # ML-based anomaly detection

├── visualize_traffic_data.py        # Interactive graphs

├── normalize_traffic_features.py    # Preprocesses features

├── TrafficAnomalyProject.net.xml   # Road network file

├── TrafficAnomalyProject.rou.xml   # Route file for vehicles

├── simulation.sumocfg              # Simulation configuration

├── README.md                       # Project documentation



Future Work
Integrate real-world IoV data for more realistic anomaly detection.
Add real-time traffic monitoring using TraCI.
Expand the road network to include multi-lane highways, weather effects, and collisions.
Explore advanced ML models (e.g., LSTMs) for time-series anomaly detection.
Acknowledgments
This project is inspired by the research paper: "Deep Learning-Based Anomaly Detection for Fog-Assisted IoVs Networks".
