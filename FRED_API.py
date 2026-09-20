from fredapi import Fred

def get_cpi_data(api_key):
    fred = Fred(api_key=api_key)
    cpi_data = fred.get_series("CPIAUCSL")
    return cpi_data

def get_employment_data(api_key):
    fred = Fred(api_key=api_key)
    employment_data = fred.get_series("PAYEMS")
    return employment_data

def get_rate_data(api_key):
    fred = Fred(api_key=api_key)
    rate_data = fred.get_series("FEDFUNDS")
    return rate_data