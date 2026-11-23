from simulator.traffic import simulate

def test_simulation():
    result = simulate(1000, 100, 700)
    assert result["passed_requests"] == 900
    assert result["origin_over_capacity"] is True
