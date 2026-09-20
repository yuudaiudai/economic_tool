def analyze_employment(employment_data, unemployment_data, hourly_earnings):

    if (
        employment_data is None or employment_data.empty
        or unemployment_data is None or unemployment_data.empty
        or hourly_earnings is None or hourly_earnings.empty
    ):
        return None, "分析不可"

    # 雇用者数前年比
    employment_yoy = employment_data.pct_change(12) * 100
    employment_yoy = employment_yoy.dropna()

    # 失業率前年比
    unemployment_yoy = unemployment_data.pct_change(12) * 100
    unemployment_yoy = unemployment_yoy.dropna()

    # 平均時給前年比
    hourly_earnings_yoy = hourly_earnings.pct_change(12) * 100
    hourly_earnings_yoy = hourly_earnings_yoy.dropna()

    if (
        len(employment_yoy) < 4
        or len(unemployment_yoy) < 4
        or len(hourly_earnings_yoy) < 4
    ):
        return None, "分析不可"

    latest_employment_yoy = employment_yoy.iloc[-1]
    latest_unemployment_yoy = unemployment_yoy.iloc[-1]
    latest_hourly_earnings_yoy = hourly_earnings_yoy.iloc[-1]

    # 3か月前比
    employment_change = latest_employment_yoy - employment_yoy.iloc[-4]
    unemployment_change = latest_unemployment_yoy - unemployment_yoy.iloc[-4]
    hourly_earnings_change = (
        latest_hourly_earnings_yoy
        - hourly_earnings_yoy.iloc[-4]
    )



    # 雇用状況
    employment_score = 0

    if latest_employment_yoy >= 0:
        employment_score += 1
    else:
        employment_score -= 1

    unemployment_score = 0

    if latest_unemployment_yoy < 0:
        unemployment_score += 1
    elif latest_unemployment_yoy > 0:
        unemployment_score -= 1

    wage_score = 0

    if latest_hourly_earnings_yoy >= 3:
        wage_score += 1
    elif latest_hourly_earnings_yoy < 0:
        wage_score -= 1

    # 雇用総合スコア
    employment_score_total = (
        employment_score
        + unemployment_score
        + wage_score
    )

    # 雇用総合判断
    if employment_score_total >= 2:
        employment_judgment = "雇用改善"
    elif employment_score_total <= -2:
        employment_judgment = "雇用悪化"
    else:
        employment_judgment = "雇用中立"



    # 雇用のトレンド
    trend_score = 0

    # 雇用者数
    if employment_change > 0.2:
        trend_score += 1
    elif employment_change < -0.2:
        trend_score -= 1

    # 失業率
    if unemployment_change < -0.2:
        trend_score += 1
    elif unemployment_change > 0.2:
        trend_score -= 1

    # 平均時給
    if hourly_earnings_change > 0.2:
        trend_score += 1
    elif hourly_earnings_change < -0.2:
        trend_score -= 1

    # 雇用トレンド総合判断
    if trend_score >= 2:
        employment_trend = "雇用改善傾向"
    elif trend_score <= -2:
        employment_trend = "雇用悪化傾向"
    else:
        employment_trend = "雇用横ばい傾向"

    return (
        latest_employment_yoy,
        latest_unemployment_yoy,
        latest_hourly_earnings_yoy,
        employment_score_total,
        employment_judgment,
        trend_score,
        employment_trend
    )