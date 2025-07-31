import json
from models.waypoint import Waypoint
from models.mission import DroneMission

def load_missions_from_json(filepath: str):
    with open(filepath, 'r') as f:
        data = json.load(f)

    missions = []
    for item in data:
        waypoints = [Waypoint(*pt['position'], pt['time']) for pt in item['waypoints']]
        missions.append(DroneMission(item['drone_id'], waypoints))
    return missions
