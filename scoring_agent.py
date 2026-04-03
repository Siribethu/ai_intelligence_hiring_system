target_roles = ["AI", "Data", "ML", "DevOps", "Backend", "Cloud"]


def score_company(company):
    score = 0
    role_count = len(company["roles"])

    # Signal 1: multiple roles
    if role_count >= 3:
        score += 40

    # Signal 2: variety of roles
    unique_roles = set(company["roles"])
    if len(unique_roles) >= 2:
        score += 20

    # Signal 3: niche roles
    for role in company["roles"]:
        for target in target_roles:
            if target.lower() in role.lower():
                score += 10

    return score


def get_reason(company):
    reasons = []

    if len(company["roles"]) >= 3:
        reasons.append("Multiple job openings")

    if any(
        ("ai" in role.lower() or "data" in role.lower())
        for role in company["roles"]
    ):
        reasons.append("Hiring niche roles")

    return ", ".join(reasons)


def score_companies(signals):
    results = {}

    for company, data in signals.items():
        score = score_company(data)
        reason = get_reason(data)

        results[company] = {
            "score": score,
            "reason": reason
        }

    # Sort by score
    sorted_results = dict(
        sorted(results.items(), key=lambda x: x[1]["score"], reverse=True)
    )

    return sorted_results