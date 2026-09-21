import sys
import os


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from overall_analyze import analyze_investment


def test_overall_good():
    result = analyze_investment(
        "インフレ",
        "インフレ加速傾向",
        "雇用改善",
        "雇用改善傾向",
        "金融引き締め"
    )

    assert result[0] == 5
    assert result[1] == "好景気"

def test_overall_bad():
    result = analyze_investment(
        "ディスインフレ",
        "インフレ鈍化傾向",
        "雇用悪化",
        "雇用悪化傾向",
        "金融緩和"
    )

    assert result[0] == -5
    assert result[1] == "不景気"

def test_overall_neutral():
    result = analyze_investment(
        "横ばい",
        "横ばい傾向",
        "雇用横ばい",
        "雇用横ばい傾向",
        "金融政策中立"
    )

    assert result[0] == 0
    assert result[1] == "中立景気"

def test_overall_good_boundary():
    result = analyze_investment(
        "インフレ",
        "インフレ加速傾向",
        "雇用改善",
        "雇用改善傾向",
        "金融政策中立"
    )

    assert result[0] == 4
    assert result[1] == "好景気"

def test_overall_bad_boundary():
    result = analyze_investment(
        "ディスインフレ",
        "インフレ鈍化傾向",
        "雇用悪化",
        "雇用悪化傾向",
        "金融政策中立"
    )

    assert result[0] == -4
    assert result[1] == "不景気"

def test_overall_invalid_cpi():
    result = analyze_investment(
        "分析不可",
        "横ばい傾向",
        "雇用改善",
        "雇用改善傾向",
        "金融引き締め"
    )

    assert result == (None, "分析不可")

def test_overall_invalid_employment():
    result = analyze_investment(
        "インフレ",
        "インフレ加速傾向",
        "分析不可",
        "雇用改善傾向",
        "金融引き締め"
    )

    assert result == (None, "分析不可")

def test_overall_invalid_rate():
    result = analyze_investment(
        "インフレ",
        "インフレ加速傾向",
        "雇用改善",
        "雇用改善傾向",
        "分析不可"
    )

    assert result == (None, "分析不可")