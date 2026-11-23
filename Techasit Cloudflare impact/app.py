from simulator.traffic import simulate
from simulator.waf import waf_decision
from simulator.rate_limit import RateLimiter

def main():
    print("Techasit Cloudflare Impact Simulator")
    print("-----------------------------------")
    requests = int(input("Requests to simulate: ") or "1000")
    origin_capacity = int(input("Origin capacity (requests): ") or "700")
    blocked = 0
    limiter = RateLimiter(limit=100, window=10)

    for i in range(requests):
        allowed_waf = waf_decision({"path": "/api", "method": "GET"})
        allowed_rate = limiter.allow("demo-client")
        if not allowed_waf or not allowed_rate:
            blocked += 1

    result = simulate(requests, blocked, origin_capacity)
    print("\nSimulation result:")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
