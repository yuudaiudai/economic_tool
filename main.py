import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FRED_API_KEY")

if not API_KEY:
    print("エラー：FRED_API_KEYが設定されていません。")
    exit()

from FRED_API import get_cpi_data, get_employment_data, get_rate_data
from cpi import analyze_cpi
from employment import analyze_employment
from official_rate import analyze_rate
from overall_analyze import analyze_investment
from report import generate_report
from history import (
    save_analysis_result,
    compare_with_previous,
    detect_economic_changes
)
from graph import (
    plot_cpi,
    plot_employment,
    plot_unemployment,
    plot_hourly_earnings,
    plot_rate
)


#CPI分析
cpi_data = get_cpi_data(API_KEY)

latest_cpi, cpi_change, cpi_judgment, cpi_trend = analyze_cpi(cpi_data)

if cpi_judgment != "分析不可":
    print(f"前年比ベースでのCPI：{latest_cpi:.2f}%")
    print(f"3か月前比ベースでのCPI：{cpi_change:.2f}%ポイント")
    print(f"CPI状況：{cpi_judgment}")
    print(f"CPIトレンド：{cpi_trend}")
    
    plot_cpi(
    cpi_data,
    cpi_judgment,
    cpi_trend
)
else:
    print("CPI分析：分析不可")

#雇用分析
employment_data, unemployment_data, hourly_earnings = get_employment_data(API_KEY)

(
    latest_employment_yoy,
    latest_unemployment_yoy,
    latest_hourly_earnings_yoy,
    employment_score,
    employment_judgment,
    employment_trend_score,
    employment_trend
) = analyze_employment(
    employment_data,
    unemployment_data,
    hourly_earnings
)

if employment_judgment != "分析不可":
    print(f"雇用者数前年比：{latest_employment_yoy:.2f}%")
    print(f"失業率前年比：{latest_unemployment_yoy:.2f}%")
    print(f"平均時給前年比：{latest_hourly_earnings_yoy:.2f}%")
    print(f"雇用スコア：{employment_score}")
    print(f"雇用状況：{employment_judgment}")
    print(f"雇用トレンドスコア：{employment_trend_score}")
    print(f"雇用トレンド：{employment_trend}")
    
    plot_employment(
    employment_data,
    employment_judgment,
    employment_trend
 )
    plot_unemployment(
    unemployment_data,
    employment_judgment,
    employment_trend
)
    plot_hourly_earnings(
    hourly_earnings,
    employment_judgment,
    employment_trend
)       
else:
    print("雇用分析：分析不可")

#金利分析
rate_data = get_rate_data(API_KEY)

(
    latest_rate,
    rate_change,
    rate_change_3m,
    rate_score,
    rate_judgment
) = analyze_rate(rate_data)

if rate_judgment != "分析不可":
    print(f"政策金利：{latest_rate:.2f}%")
    print(f"前年比ベースの金利差：{rate_change:.2f}%ポイント")
    print(f"3か月前比ベースの金利差：{rate_change_3m:.2f}%ポイント")
    print(f"金利スコア：{rate_score}")
    print(f"金融政策：{rate_judgment}")
    
    plot_rate(
    rate_data,
    rate_judgment
)
else:
    print("金利分析：分析不可")
    

#総合分析
score, overall_judgment = analyze_investment(
    cpi_judgment,
    cpi_trend,
    employment_judgment,
    employment_trend,
    rate_judgment
)


print(f"総合スコア：{score}")
print(f"総合分析：{overall_judgment}")


# 過去の分析結果と比較
compare_with_previous(
    cpi_judgment,
    cpi_trend,
    employment_judgment,
    employment_trend,
    rate_judgment,
    score,
    overall_judgment
)

# 経済状態の変化を検出
changes = detect_economic_changes(
    cpi_judgment,
    cpi_trend,
    employment_judgment,
    employment_trend,
    rate_judgment,
    score,
    overall_judgment
)

# 分析レポートを作成
generate_report(
    cpi_judgment,
    cpi_trend,
    employment_judgment,
    employment_trend,
    rate_judgment,
    score,
    overall_judgment,
    changes
)

# 分析結果をcsvに保存
save_analysis_result(
    cpi_judgment,
    cpi_trend,
    employment_judgment,
    employment_trend,
    rate_judgment,
    score,
    overall_judgment
)