import traci

# Start SUMO with TraCI
traci.start(["sumo-gui", "-c", "simulation.sumocfg"])

while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
    for veh_id in traci.vehicle.getIDList():
        speed = traci.vehicle.getSpeed(veh_id)
        if speed > 20:  # Anomaly: Speed > 20 m/s
            traci.vehicle.setColor(veh_id, (255, 0, 0))  # Red
        else:
            traci.vehicle.setColor(veh_id, (0, 255, 0))  # Green

traci.close()
