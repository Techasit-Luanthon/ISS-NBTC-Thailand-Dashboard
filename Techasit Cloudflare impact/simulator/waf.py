def waf_decision(request):
    # Safe local simulation: no real network traffic is generated.
    suspicious_paths = {"/admin-test", "/malicious-test"}
    return request.get("path") not in suspicious_paths
