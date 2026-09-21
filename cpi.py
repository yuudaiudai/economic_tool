from config import (
    CPI_INFLATION_THRESHOLD,
    CPI_DISINFLATION_THRESHOLD,
    CPI_TREND_INCREASE_THRESHOLD,
    CPI_TREND_DECREASE_THRESHOLD
)


def analyze_cpi(cpi_data):

    if cpi_data is None or cpi_data.empty:
        return None, "分析不可"

    cpi_data = cpi_data.dropna()

    if len(cpi_data) < 13:
        return None, "分析不可"

    # CPI前年比
    cpi_yoy = cpi_data.pct_change(12) * 100
    cpi_yoy = cpi_yoy.dropna()

    if cpi_yoy.empty:
        return None, "分析不可"

    latest_cpi = cpi_yoy.iloc[-1]

    # CPI3か月前比
    cpi_change = latest_cpi - cpi_yoy.iloc[-4]

    # CPI状況
    if latest_cpi >= CPI_INFLATION_THRESHOLD:
        judgment = "インフレ"
    elif latest_cpi >= CPI_DISINFLATION_THRESHOLD:
        judgment = "横ばい"
    else:
        judgment = "ディスインフレ"

    # CPIトレンド
    if cpi_change > CPI_TREND_INCREASE_THRESHOLD:
        trend = "インフレ加速傾向"
    elif cpi_change < CPI_TREND_DECREASE_THRESHOLD:
        trend = "インフレ鈍化傾向"
    else:
        trend = "横ばい傾向"

    return latest_cpi, cpi_change, judgment, trend