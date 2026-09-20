def analyze_employment(employment_data):

    employment_change = employment_data.diff()
    employment_change = employment_change.dropna()
    latest_change = employment_change.iloc[-1]

    if latest_change > 0:
        judgment = "雇用改善"
    else:
        judgment = "雇用悪化"

    return latest_change, judgment