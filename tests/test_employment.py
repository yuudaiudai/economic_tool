import sys
import os


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import pandas as pd

from employment import analyze_employment


# テスト用の前年比データを作成する
def create_data(yoy_values):
    data = [100] * 12

    for yoy in yoy_values:
        data.append(100 * (1 + yoy / 100))

    return pd.Series(data)

# 雇用状況が雇用改善になることを確認
def test_employment_improvement():

    employment_data = create_data([1, 1, 1, 1])
    unemployment_data = create_data([-1, -1, -1, -1])
    hourly_earnings = create_data([3, 3, 3, 3])

    result = analyze_employment(
        employment_data,
        unemployment_data,
        hourly_earnings
    )

    assert result[4] == "雇用改善"

# 雇用状況が雇用横ばいになることを確認
def test_employment_neutral():

    employment_data = create_data([1, 1, 1, 1])
    unemployment_data = create_data([1, 1, 1, 1])
    hourly_earnings = create_data([1, 1, 1, 1])

    result = analyze_employment(
        employment_data,
        unemployment_data,
        hourly_earnings
    )

    assert result[4] == "雇用横ばい"

# 雇用状況が雇用悪化になることを確認
def test_employment_decline():

    employment_data = create_data([-1, -1, -1, -1])
    unemployment_data = create_data([1, 1, 1, 1])
    hourly_earnings = create_data([-1, -1, -1, -1])

    result = analyze_employment(
        employment_data,
        unemployment_data,
        hourly_earnings
    )

    assert result[4] == "雇用悪化"

# 雇用トレンドが改善傾向になることを確認
def test_employment_trend_improvement():

    employment_data = create_data([1, 1, 1, 1])
    unemployment_data = create_data([1, 0.5, 0, -1])
    hourly_earnings = create_data([1, 1.5, 2, 3])

    result = analyze_employment(
        employment_data,
        unemployment_data,
        hourly_earnings
    )

    assert result[6] == "雇用改善傾向"

# 雇用トレンドが横ばい傾向になることを確認
def test_employment_trend_neutral():

    employment_data = create_data([1, 1, 1, 1])
    unemployment_data = create_data([1, 1, 1, 1])
    hourly_earnings = create_data([1, 1, 1, 1])

    result = analyze_employment(
        employment_data,
        unemployment_data,
        hourly_earnings
    )

    assert result[6] == "雇用横ばい傾向"

# 雇用トレンドが悪化傾向になることを確認
def test_employment_trend_decline():

    employment_data = create_data([1, 0.5, 0, -1])
    unemployment_data = create_data([-1, 0, 0.5, 1])
    hourly_earnings = create_data([3, 2, 1, -1])

    result = analyze_employment(
        employment_data,
        unemployment_data,
        hourly_earnings
    )

    assert result[6] == "雇用悪化傾向"

# いずれかのデータがNoneの場合、分析不可になることを確認
def test_employment_none():

    employment_data = create_data([1, 1, 1, 1])
    unemployment_data = create_data([1, 1, 1, 1])

    result = analyze_employment(
        employment_data,
        unemployment_data,
        None
    )

    assert result[0] is None
    assert result[1] == "分析不可"

# いずれかのデータが空の場合、分析不可になることを確認
def test_employment_empty():

    employment_data = create_data([1, 1, 1, 1])
    unemployment_data = create_data([1, 1, 1, 1])
    hourly_earnings = pd.Series(dtype=float)

    result = analyze_employment(
        employment_data,
        unemployment_data,
        hourly_earnings
    )

    assert result[0] is None
    assert result[1] == "分析不可"

# 必要なデータの不足時、分析不可になることを確認
def test_employment_insufficient_data():

    employment_data = pd.Series([100] * 12)
    unemployment_data = pd.Series([100] * 12)
    hourly_earnings = pd.Series([100] * 12)

    result = analyze_employment(
        employment_data,
        unemployment_data,
        hourly_earnings
    )

    assert result[0] is None
    assert result[1] == "分析不可"