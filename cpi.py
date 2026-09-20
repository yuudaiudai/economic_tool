def analyze_cpi(cpi_data):

    if cpi_data is None or cpi_data.empty:
        return None, "分析不可"

    cpi_yoy = cpi_data.pct_change(12) * 100
    cpi_yoy = cpi_yoy.dropna()

    if cpi_yoy.empty:
        return None, "分析不可"

    latest_cpi = cpi_yoy.iloc[-1]

    if latest_cpi > 3:
        judgment = "インフレ"
    elif latest_cpi >= 0.5:
        judgment = "中立水準"
    else:
        judgment = "ディスインフレ"

    return latest_cpi, judgment