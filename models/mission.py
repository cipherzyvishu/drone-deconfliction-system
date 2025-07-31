from typing import List
from .waypoint import Waypoint

class DroneMission:
    def __init__(self, drone_id: str, waypoints: List[Waypoint]):
        self.drone_id = drone_id
        self.waypoints = waypoints

    def get_segments(self):
        return [(self.waypoints[i], self.waypoints[i + 1]) for i in range(len(self.waypoints) - 1)]
