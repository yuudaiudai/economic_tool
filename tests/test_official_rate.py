import sys
import os


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import pandas as pd

from official_rate import analyze_rate


# テスト用の金利データを作成する
def create_rate_data(values):
    data = [3.0] * 12

    for value in values:
        data.append(value)

    return pd.Series(data)

# 政策金利が3.75%以上なら高金利になることを確認
def test_rate_high():

    rate_data = create_rate_data([4.0, 4.0, 4.0, 4.0])

    result = analyze_rate(rate_data)

    assert result[0] == 4.0
    assert result[3] >= 1

# 政策金利が2.0%以上3.75%未満なら中立金利になることを確認
def test_rate_neutral():

    rate_data = create_rate_data([3.0, 3.0, 3.0, 3.0])

    result = analyze_rate(rate_data)

    assert result[0] == 3.0

# 政策金利が2.0%未満なら低金利になることを確認
def test_rate_low():

    rate_data = create_rate_data([1.0, 1.0, 1.0, 1.0])

    result = analyze_rate(rate_data)

    assert result[0] == 1.0
    assert result[3] <= -1

# 3か月前比較0.25ポイント超上昇している場合、金融引き締めになることを確認
def test_rate_hike():

    rate_data = create_rate_data([
        3.0,
        3.0,
        3.0,
        3.5
    ])

    result = analyze_rate(rate_data)

    assert result[2] == 0.5
    assert result[4] == "金融引き締め"

# 3か月前比で0.25ポイント超低下している場合、金融緩和になることを確認
def test_rate_cut():

    rate_data = create_rate_data([
        3.0,
        3.0,
        3.0,
        2.5
    ])

    result = analyze_rate(rate_data)

    assert result[2] == -0.5
    assert result[4] == "金融緩和"

# 金利水準と金利トレンドから、金融政策中立になることを確認
def test_rate_neutral_policy():

    rate_data = create_rate_data([
        3.0,
        3.0,
        3.0,
        3.0
    ])

    result = analyze_rate(rate_data)

    assert result[3] == 0
    assert result[4] == "金融政策中立"

# 金利データがNoneの場合、分析不可になることを確認
def test_rate_none():

    result = analyze_rate(None)

    assert result == (None, "分析不可")

# 金利データが空の場合、分析不可になることを確認
def test_rate_empty():

    rate_data = pd.Series(dtype=float)

    result = analyze_rate(rate_data)

    assert result == (None, "分析不可")
    
# 金利データが13か月未満の場合、分析不可になることを確認
def test_rate_insufficient_data():

    rate_data = pd.Series([3.0] * 12)

    result = analyze_rate(rate_data)

    assert result == (None, "分析不可")