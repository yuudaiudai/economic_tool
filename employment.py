def analyze_employment(employment_data):

    if employment_data is None or employment_data.empty:
        return None, "分析不可"

    employment_change = employment_data.diff()
    employment_change = employment_change.dropna()

    if employment_change.empty:
        return None, "分析不可"

    latest_change = employment_change.iloc[-1]

    if latest_change > 0:
        judgment = "雇用改善"
    elif latest_change == 0:
        judgment = "雇用変化なし"
    elif latest_change <0:
        judgment = "雇用悪化"

    return latest_change, judgment