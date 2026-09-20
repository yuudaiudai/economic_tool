def analyze_investment(
    cpi_judgment,
    cpi_trend,
    employment_judgment,
    employment_trend,
    rate_judgment
):


    # 入力値チェック
    if (
        cpi_judgment == "分析不可"
        or employment_judgment == "分析不可"
        or rate_judgment == "分析不可"
    ):
        return None, "分析不可"

    score = 0


    # CPI
    cpi_score = 0

    # CPIの状態
    if cpi_judgment == "インフレ":
        cpi_score += 1
    elif cpi_judgment == "ディスインフレ":
        cpi_score -= 1

    # CPIのトレンド
    if cpi_trend == "インフレ傾向":
        cpi_score += 1
    elif cpi_trend == "ディスインフレ傾向":
        cpi_score -= 1

    score += cpi_score
    

    # 雇用
    employment_score = 0

    # 雇用の状態
    if employment_judgment == "雇用改善":
        employment_score += 1
    elif employment_judgment == "雇用悪化":
        employment_score -= 1

    # 雇用のトレンド
    if employment_trend == "雇用改善傾向":
        employment_score += 1
    elif employment_trend == "雇用悪化傾向":
        employment_score -= 1

    score += employment_score
    

    # 金利
    rate_score = 0

    # 金融政策
    if rate_judgment == "金融引き締め":
        rate_score += 1
    elif rate_judgment == "金融緩和":
        rate_score -= 1
        
    score += rate_score


    # 総合判断
    if score >= 4:
        overall_judgment = "好景気"
    elif score <= -4:
        overall_judgment = "不景気"
    else:
        overall_judgment = "中立景気"

    return score, overall_judgment