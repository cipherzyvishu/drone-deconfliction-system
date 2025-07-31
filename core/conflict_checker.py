from core.spatial import segment_to_segment_distance
from models.mission import DroneMission
from core.temporal import check_temporal_overlap



class ConflictChecker:
    def __init__(self, safety_distance=10.0, time_threshold=2.0):
        self.safety_distance = safety_distance
        self.time_threshold = time_threshold

    def check_spatio_temporal_conflicts(self, primary: DroneMission, others: list):
        conflicts = []
        primary_segs = primary.get_segments()

        for other in others:
            other_segs = other.get_segments()
            for p1, p2 in primary_segs:
                for q1, q2 in other_segs:
                    dist, cp1, cp2 = segment_to_segment_distance(p1, p2, q1, q2)
                    if dist < self.safety_distance:
                        if check_temporal_overlap(p1.t, p2.t, q1.t, q2.t, self.time_threshold):
                            conflicts.append({
                                "conflict_with": other.drone_id,
                                "distance": dist,
                                "point_on_primary": cp1.tolist(),
                                "point_on_other": cp2.tolist(),
                                "primary_time_range": (p1.t, p2.t),
                                "other_time_range": (q1.t, q2.t)
                            })

        return conflicts
