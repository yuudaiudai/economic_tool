import sys
import os


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import pandas as pd
from cpi import analyze_cpi


def create_cpi_data(yoy_values):
    """テスト用のCPIデータを作成する"""
    data = [100] * 12

    for yoy in yoy_values:
        data.append(100 * (1 + yoy / 100))

    return pd.Series(data)

def test_cpi_inflation():
    """CPI前年比が2.0%以上ならインフレになることを確認"""
    cpi_data = create_cpi_data([2.5, 2.5, 2.5, 2.5])

    latest_cpi, cpi_change, judgment, trend = analyze_cpi(cpi_data)

    assert judgment == "インフレ"

def test_cpi_neutral():
    """CPI前年比が0.55%以上2.0%未満なら横ばいになることを確認"""
    cpi_data = create_cpi_data([1.0, 1.0, 1.0, 1.0])

    latest_cpi, cpi_change, judgment, trend = analyze_cpi(cpi_data)

    assert judgment == "横ばい"

def test_cpi_disinflation():
    """CPI前年比が0.55%未満ならディスインフレになることを確認"""
    cpi_data = create_cpi_data([0.3, 0.3, 0.3, 0.3])

    latest_cpi, cpi_change, judgment, trend = analyze_cpi(cpi_data)

    assert judgment == "ディスインフレ"

def test_cpi_none():
    """CPIデータがNoneの場合、分析不可になることを確認"""
    result = analyze_cpi(None)

    assert result == (None, "分析不可")

def test_cpi_empty():
    """CPIデータが空の場合、分析不可になることを確認"""
    cpi_data = pd.Series(dtype=float)

    result = analyze_cpi(cpi_data)

    assert result == (None, "分析不可")

def test_cpi_insufficient_data():
    """CPIデータが13か月未満の場合、分析不可になることを確認"""
    cpi_data = pd.Series([100] * 12)

    result = analyze_cpi(cpi_data)

    assert result == (None, "分析不可")