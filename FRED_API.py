from fredapi import Fred


def get_cpi_data(api_key):
    try:
        fred = Fred(api_key=api_key)
        cpi_data = fred.get_series("CPIAUCSL")
        return cpi_data
    except Exception as e:
        print(f"CPIデータの取得に失敗しました：{e}")
        return None

def get_employment_data(api_key):
    try:
        fred = Fred(api_key=api_key)

        employment_data = fred.get_series("PAYEMS")
        unemployment_data = fred.get_series("UNRATE")
        hourly_earnings = fred.get_series("CES0500000003")

        return employment_data, unemployment_data, hourly_earnings

    except Exception as e:
        print(f"雇用データの取得に失敗しました：{e}")
        return None, None, None

def get_rate_data(api_key):
    try:
        fred = Fred(api_key=api_key)
        rate_data = fred.get_series("FEDFUNDS")
        return rate_data
    except Exception as e:
        print(f"金利データの取得に失敗しました：{e}")
        return None