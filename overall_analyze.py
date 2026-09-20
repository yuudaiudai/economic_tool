def analyze_investment(cpi_judgment, employment_judgment, rate_judgment):

    score = 0

    # CPIの評価
    if cpi_judgment == "インフレ":
        score += 1
    elif cpi_judgment == "中立水準":
        score = 0
    elif cpi_judgment == "インフレ圧力：低":
        score -= 1

    # 雇用の評価
    if employment_judgment == "雇用改善":
        score += 1
    elif employment_judgment == "雇用悪化":
        score -= 1

    # 金利の評価
    if rate_judgment == "高金利":
        score += 1
    elif rate_judgment == "中立金利":
        score = 0
    elif rate_judgment == "低金利":
        score -= 1

    # 総合判断
    if score >= 2:
        overall_judgment = "好景気"
    elif score <= -2:
        overall_judgment = "悪景気"
    else:
        overall_judgment = "中立景気"

    return score, overall_judgment