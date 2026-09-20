def analyze_investment(cpi_judgment, employment_judgment, rate_judgment):
    
    if (
    cpi_judgment == "分析不可"
    or employment_judgment == "分析不可"
    or rate_judgment == "分析不可"
    ):
        return None, "分析不可"

    score = 0

    # CPI
    if cpi_judgment == "インフレ":
        score += 1
    elif cpi_judgment == "中立水準":
        pass
    elif cpi_judgment == "ディスインフレ":
        score -= 1

    # 雇用
    if employment_judgment == "雇用改善":
        score += 1
    elif employment_judgment == "雇用変化なし":
        pass
    elif employment_judgment == "雇用悪化":
        score -= 1

    # 金利
    if rate_judgment == "高金利":
        score += 1
    elif rate_judgment == "中立金利":
        pass
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