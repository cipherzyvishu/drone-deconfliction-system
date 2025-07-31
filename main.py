from utils.data_loader import load_missions_from_json
from core.conflict_checker import ConflictChecker
from utils.visualizer import visualize_missions

if __name__ == "__main__":
    missions = load_missions_from_json("data/sample_missions.json")
    primary = missions[0]
    others = missions[1:]

    checker = ConflictChecker()
    conflicts = checker.check_spatio_temporal_conflicts(primary, others)

    for c in conflicts:
        print(f"[!] Conflict with {c['conflict_with']} at distance {c['distance']:.2f}m")
        print(f"  Times: {c['primary_time_range']} vs {c['other_time_range']}")
        print(f"  Points: {c['point_on_primary']} ↔ {c['point_on_other']}\n")

    visualize_missions(missions, conflicts)
