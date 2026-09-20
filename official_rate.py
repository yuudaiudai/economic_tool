def analyze_rate(rate_data):

    if rate_data is None or rate_data.empty:
        return None, None, None, None, "分析不可能"

    rate_data = rate_data.dropna()

    if len(rate_data) < 13:
        return None, None, None, None, "分析不可能"

    # 最新の政策金利
    latest_rate = rate_data.iloc[-1]

    # 1年前との金利差
    rate_change = latest_rate - rate_data.iloc[-13]

    # 3か月前との金利差
    rate_change_3m = latest_rate - rate_data.iloc[-4]


    # 金利水準
    if latest_rate >= 3.75:
        rate_level = "高金利"
    elif latest_rate >= 2.0:
        rate_level = "中立金利"
    else:
        rate_level = "低金利"

    # 金利トレンド
    if rate_change_3m > 0.25:
        rate_trend = "利上げ"
    elif rate_change_3m < -0.25:
        rate_trend = "利下げ"
    else:
        rate_trend = "金利横ばい"

    # 金利スコア
    rate_score = 0

    # 金利水準
    if rate_level == "高金利":
        rate_score += 1
    elif rate_level == "低金利":
        rate_score -= 1

    # 金利トレンド
    if rate_trend == "利上げ":
        rate_score += 1
    elif rate_trend == "利下げ":
        rate_score -= 1
        

    # 金融政策判断
    if rate_score >= 1:
        rate_judgment = "金融引き締め"
    elif rate_score <= -1:
        rate_judgment = "金融緩和"
    else:
        rate_judgment = "金融政策中立"

    return (
        latest_rate,
        rate_change,
        rate_change_3m,
        rate_score,
        rate_judgment
    )