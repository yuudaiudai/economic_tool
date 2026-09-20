def analyze_rate(rate_data):

    if rate_data is None or rate_data.empty:
        return None, "分析不可"

    rate_data = rate_data.dropna()

    if rate_data.empty:
        return None, "分析不可"

    latest_rate = rate_data.iloc[-1]

    if latest_rate >= 3.75:
        judgment = "高金利"
    elif latest_rate >= 2.25:
        judgment = "中立金利"
    else:
        judgment = "低金利"

    return latest_rate, judgment