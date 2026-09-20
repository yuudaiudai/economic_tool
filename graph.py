import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["font.family"] = "Hiragino Sans"


# CPI
def plot_cpi(cpi_data, judgment, trend):

    cpi_yoy = cpi_data.pct_change(12) * 100
    cpi_yoy = cpi_yoy.dropna()

    latest_cpi = cpi_yoy.iloc[-1]

    plt.figure(figsize=(10, 5))

    plt.plot(
        cpi_yoy.index,
        cpi_yoy.values
    )
    
    plt.axhline(
    0.55,
    linestyle="--",
    linewidth=1
    )
    
    plt.axhline(
    2.0,
    linestyle="--",
    linewidth=1
    )

    plt.title("消費者物価指数（前年比ベース）")
    plt.xlabel("年月")
    plt.ylabel("消費者物価指数(%)")

    plt.text(
        0.02,
        0.95,
        f"Latest: {latest_cpi:.2f}%\nJudgment: {judgment}\nTrend: {trend}",
        transform=plt.gca().transAxes,
        verticalalignment="top"
    )

    plt.grid(True)
    plt.tight_layout()

    plt.show()


# 雇用者数
def plot_employment(employment_data, judgment, trend):

    employment_yoy = employment_data.pct_change(12) * 100
    employment_yoy = employment_yoy.dropna()

    latest_employment = employment_yoy.iloc[-1]

    plt.figure(figsize=(10, 5))

    plt.plot(
        employment_yoy.index,
        employment_yoy.values
    )

    plt.title("雇用者数（前年比ベース）")
    plt.xlabel("年月")
    plt.ylabel("雇用者数 (%)")

    plt.text(
        0.02,
        0.95,
        f"Latest: {latest_employment:.2f}%\nJudgment: {judgment}\nTrend: {trend}",
        transform=plt.gca().transAxes,
        verticalalignment="top"
    )

    plt.grid(True)
    plt.tight_layout()

    plt.show()


# 失業率
def plot_unemployment(unemployment_data, judgment, trend):

    unemployment_yoy = unemployment_data.pct_change(12) * 100
    unemployment_yoy = unemployment_yoy.dropna()

    latest_unemployment = unemployment_yoy.iloc[-1]

    plt.figure(figsize=(10, 5))

    plt.plot(
        unemployment_yoy.index,
        unemployment_yoy.values
    )

    plt.title("失業率(前年比ベース)")
    plt.xlabel("年月")
    plt.ylabel("失業率 (%)")

    plt.text(
        0.02,
        0.95,
        f"Latest: {latest_unemployment:.2f}%\n"
        f"Judgment: {judgment}\n"
        f"Trend: {trend}",
        transform=plt.gca().transAxes,
        verticalalignment="top"
    )

    plt.grid(True)
    plt.tight_layout()

    plt.show()


# 平均時給
def plot_hourly_earnings(hourly_earnings, judgment, trend):

    hourly_earnings_yoy = hourly_earnings.pct_change(12) * 100
    hourly_earnings_yoy = hourly_earnings_yoy.dropna()

    latest_hourly_earnings = hourly_earnings_yoy.iloc[-1]

    plt.figure(figsize=(10, 5))

    plt.plot(
        hourly_earnings_yoy.index,
        hourly_earnings_yoy.values
    )

    plt.title("平均時給（前年比ベース）")
    plt.xlabel("年月")
    plt.ylabel("平均時給(%)")

    plt.text(
        0.02,
        0.95,
        f"Latest: {latest_hourly_earnings:.2f}%\n"
        f"Judgment: {judgment}\n"
        f"Trend: {trend}",
        transform=plt.gca().transAxes,
        verticalalignment="top"
    )

    plt.grid(True)
    plt.tight_layout()

    plt.show()


# 政策金利
def plot_rate(rate_data, judgment):

    rate_data = rate_data.dropna()

    latest_rate = rate_data.iloc[-1]

    plt.figure(figsize=(10, 5))

    plt.plot(
        rate_data.index,
        rate_data.values
    )
    
    plt.axhline(
    2.0,
    linestyle="--",
    linewidth=1
    )
    
    plt.axhline(
    3.75,
    linestyle="--",
    linewidth=1
    )

    plt.title("政策金利（前年比ベース）")
    plt.xlabel("年月")
    plt.ylabel("政策金利 (%)")

    plt.text(
        0.02,
        0.95,
        f"Latest: {latest_rate:.2f}%\nJudgment: {judgment}",
        transform=plt.gca().transAxes,
        verticalalignment="top"
    )

    plt.grid(True)
    plt.tight_layout()

    plt.show()