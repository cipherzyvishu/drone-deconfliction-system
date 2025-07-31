def check_temporal_overlap(t1_start, t1_end, t2_start, t2_end, threshold=2.0):
    """
    Checks if two time intervals overlap within a given threshold (in seconds).
    This accounts for slight overlaps due to rounding or interpolation drift.
    """
    latest_start = max(t1_start, t2_start)
    earliest_end = min(t1_end, t2_end)
    overlap_duration = earliest_end - latest_start

    return overlap_duration >= -threshold  # overlap or near overlap
