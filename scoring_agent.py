from collections import Counter

# Target niche roles
target_roles = ["AI", "Data", "ML", "DevOps", "Backend", "Cloud"]


# 🟡 1. SIGNAL-BASED SCORING
def score_company(data):
    score = 0
    reasons = []

    roles = data["roles"]
    total_jobs = len(roles)

    # Signal 1: multiple job postings
    if total_jobs >= 3:
        score += 30
        reasons.append("Multiple job openings")

    # Signal 2: repeated roles (hiring aggressively)
    role_freq = Counter(roles)
    repeated_roles = sum(1 for r, c in role_freq.items() if c > 1)

    if repeated_roles >= 1:
        score += 25
        reasons.append("Repeated hiring for same role")

    # Signal 3: niche roles (AI/Data/etc.)
    niche_roles = sum(
        1 for role in roles
        for target in target_roles
        if target.lower() in role.lower()
    )

    if niche_roles >= 2:
        score += 20
        reasons.append("Hiring niche roles")

    return score, reasons


# 🟢 2. ICP FILTERING
def apply_icp(data):
    icp_score = 0
    icp_reasons = []

    # Ideal company size (small-mid companies)
    if 20 <= data["size"] <= 500:
        icp_score += 30
        icp_reasons.append("Ideal company size")

    # Relevant industry
    if str(data["industry"]).lower() in ["ai", "tech", "saas"]:
        icp_score += 20
        icp_reasons.append("Relevant industry")

    return icp_score, icp_reasons


# 🔵 3. FINAL MERGE + OUTPUT
def score_companies(signals, df):
    results = {}

    for company, data in signals.items():

        # 1. Signal scoring
        score, reasons = score_company(data)

        # 2. ICP scoring
        company_row = df[df['company'] == company].iloc[0]

        icp_data = {
            "size": company_row["size"],
            "industry": company_row["industry"]
        }

        icp_score, icp_reasons = apply_icp(icp_data)

        # 3. Final score
        total_score = score + icp_score

        # 4. Combine reasons
        all_reasons = reasons + icp_reasons

        # 5. Default fallback reason (VERY IMPORTANT)
        if not all_reasons:
            all_reasons = ["Low hiring activity or not matching ICP"]

        results[company] = {
            "score": total_score,
            "reason": ", ".join(all_reasons)
        }

    # 6. Sort by score (descending)
    return dict(
        sorted(results.items(), key=lambda x: x[1]["score"], reverse=True)
    )
