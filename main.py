import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FRED_API_KEY")

from FRED_API import get_cpi_data, get_employment_data, get_rate_data
from cpi import analyze_cpi
from employment import analyze_employment
from official_rate import analyze_rate
from overall_analyze import analyze_investment

#CPi分析
cpi_data = get_cpi_data(API_KEY)

latest_cpi, cpi_judgment = analyze_cpi(cpi_data)

print(f"CPI前年比：{latest_cpi:.2f}%")
print(f"CPI状況：{cpi_judgment}")

#雇用分析
employment_data = get_employment_data(API_KEY)

latest_change, employment_judgment = analyze_employment(employment_data)

print(f"雇用者数の前月比：{latest_change:.0f}千人")
print(f"雇用状況：{employment_judgment}")

#金利分析
rate_data = get_rate_data(API_KEY)

latest_rate, rate_judgment = analyze_rate(rate_data)

print(f"政策金利：{latest_rate:.2f}%")
print(f"金利状況：{rate_judgment}")

#総合分析
score, overall_judgment = analyze_investment(
    cpi_judgment,
    employment_judgment,
    rate_judgment
)

print(f"総合スコア：{score}")
print(f"総合分析：{overall_judgment}")