from config import (
    RATE_HIGH_THRESHOLD,
    RATE_NEUTRAL_THRESHOLD,
    RATE_HIKE_THRESHOLD,
    RATE_CUT_THRESHOLD
)


def analyze_rate(rate_data):

    if rate_data is None or rate_data.empty:
        return None, "分析不可"

    rate_data = rate_data.dropna()

    if len(rate_data) < 13:
        return None, "分析不可"

    # 最新の政策金利
    latest_rate = rate_data.iloc[-1]

    # 前年比ベースの金利差
    rate_change = latest_rate - rate_data.iloc[-13]

    # 3か月前比ベースの金利差
    rate_change_3m = latest_rate - rate_data.iloc[-4]

    # 現在の金利状況
    if latest_rate >= RATE_HIGH_THRESHOLD:
        rate_level = "高金利"
    elif latest_rate >= RATE_NEUTRAL_THRESHOLD:
        rate_level = "中立金利"
    else:
        rate_level = "低金利"

    # 金利3ヶ月前比状況
    if rate_change_3m > RATE_HIKE_THRESHOLD:
        rate_trend = "利上げ"
    elif rate_change_3m < RATE_CUT_THRESHOLD:
        rate_trend = "利下げ"
    else:
        rate_trend = "金利横ばい"

    # 金利スコア
    rate_score = 0

    # 現在の金利スコアリング
    if rate_level == "高金利":
        rate_score += 1
    elif rate_level == "低金利":
        rate_score -= 1

    # 金利3ヶ月前比スコアリング
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