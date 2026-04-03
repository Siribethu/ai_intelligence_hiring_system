def detect_signals(df):
    signals = {}

    for company in df['company'].unique():
        company_data = df[df['company'] == company]

        roles = company_data['role'].tolist()

        signals[company] = {
            "roles": roles,
            "total_jobs": len(roles)
        }

    return signals