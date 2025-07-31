import numpy as np
from models.waypoint import Waypoint

SMALL_NUM = 1e-8

def segment_to_segment_distance(P1: Waypoint, P2: Waypoint, Q1: Waypoint, Q2: Waypoint):
    u = np.array([P2.x - P1.x, P2.y - P1.y, P2.z - P1.z])
    v = np.array([Q2.x - Q1.x, Q2.y - Q1.y, Q2.z - Q1.z])
    w0 = np.array([P1.x - Q1.x, P1.y - Q1.y, P1.z - Q1.z])

    a = np.dot(u, u)
    b = np.dot(u, v)
    c = np.dot(v, v)
    d = np.dot(u, w0)
    e = np.dot(v, w0)

    denom = a * c - b * b

    if abs(denom) < SMALL_NUM:
        sc = 0.0
        tc = e / c if c > SMALL_NUM else 0.0
    else:
        sc = (b * e - c * d) / denom
        tc = (a * e - b * d) / denom

    sc = max(0.0, min(1.0, sc))
    tc = max(0.0, min(1.0, tc))

    point_on_P = np.array([P1.x, P1.y, P1.z]) + sc * u
    point_on_Q = np.array([Q1.x, Q1.y, Q1.z]) + tc * v
    distance = np.linalg.norm(point_on_P - point_on_Q)

    return distance, point_on_P, point_on_Q
