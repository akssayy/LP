def ml_agent(hours):
    score = m * hours + c
    return "PASS" if score >= 60 else "FAIL"

ml_agent(6)