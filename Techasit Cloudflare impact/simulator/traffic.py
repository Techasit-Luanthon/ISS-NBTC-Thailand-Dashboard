def simulate(total_requests, blocked_requests, origin_capacity):
    passed = max(total_requests - blocked_requests, 0)
    origin_load = min(passed / max(origin_capacity, 1), 1.0)
    return {
        "total_requests": total_requests,
        "blocked_requests": blocked_requests,
        "passed_requests": passed,
        "origin_load_percent": round(origin_load * 100, 2),
        "origin_over_capacity": passed > origin_capacity,
    }
