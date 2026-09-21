import sys
import os


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import csv
import history

def test_save_analysis_result(tmp_path, monkeypatch):
    test_file = tmp_path / "analysis_history.csv"

    monkeypatch.setattr(history, "HISTORY_FILE", str(test_file))

    history.save_analysis_result(
        "インフレ",
        "インフレ加速傾向",
        "雇用改善",
        "雇用改善傾向",
        "金融引き締め",
        5,
        "好景気"
    )

    assert test_file.exists()

    with open(test_file, "r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == 1
    assert rows[0]["cpi_judgment"] == "インフレ"
    assert rows[0]["employment_judgment"] == "雇用改善"
    assert rows[0]["rate_judgment"] == "金融引き締め"
    assert rows[0]["score"] == "5"
    assert rows[0]["overall_judgment"] == "好景気"

def test_get_previous_result(tmp_path, monkeypatch):
    test_file = tmp_path / "analysis_history.csv"

    monkeypatch.setattr(history, "HISTORY_FILE", str(test_file))

    history.save_analysis_result(
        "インフレ",
        "インフレ加速傾向",
        "雇用改善",
        "雇用改善傾向",
        "金融引き締め",
        5,
        "好景気"
    )

    result = history.get_previous_result()

    assert result is not None
    assert result["cpi_judgment"] == "インフレ"
    assert result["score"] == "5"
    assert result["overall_judgment"] == "好景気"

def test_get_previous_result_when_file_not_exists(tmp_path, monkeypatch):
    test_file = tmp_path / "analysis_history.csv"

    monkeypatch.setattr(history, "HISTORY_FILE", str(test_file))

    result = history.get_previous_result()

    assert result is None

def test_get_previous_result_when_file_is_empty(tmp_path, monkeypatch):
    test_file = tmp_path / "analysis_history.csv"
    test_file.write_text("", encoding="utf-8")

    monkeypatch.setattr(history, "HISTORY_FILE", str(test_file))

    result = history.get_previous_result()

    assert result is None

def test_compare_with_previous(tmp_path, monkeypatch, capsys):
    test_file = tmp_path / "analysis_history.csv"

    monkeypatch.setattr(history, "HISTORY_FILE", str(test_file))

    history.save_analysis_result(
        "インフレ",
        "横ばい傾向",
        "雇用横ばい",
        "雇用横ばい傾向",
        "金融政策中立",
        0,
        "中立景気"
    )

    history.compare_with_previous(
        "インフレ",
        "インフレ加速傾向",
        "雇用改善",
        "雇用改善傾向",
        "金融引き締め",
        5,
        "好景気"
    )

    captured = capsys.readouterr()

    assert "CPIトレンド：横ばい傾向 → インフレ加速傾向" in captured.out
    assert "雇用状況：雇用横ばい → 雇用改善" in captured.out
    assert "総合スコア：0 → 5" in captured.out
    assert "総合分析：中立景気 → 好景気" in captured.out

def test_detect_economic_changes(tmp_path, monkeypatch):
    test_file = tmp_path / "analysis_history.csv"

    monkeypatch.setattr(history, "HISTORY_FILE", str(test_file))

    history.save_analysis_result(
        "インフレ",
        "横ばい傾向",
        "雇用横ばい",
        "雇用横ばい傾向",
        "金融政策中立",
        0,
        "中立景気"
    )

    changes = history.detect_economic_changes(
        "インフレ",
        "インフレ加速傾向",
        "雇用改善",
        "雇用改善傾向",
        "金融引き締め",
        5,
        "好景気"
    )

    assert len(changes) == 6
    assert "CPIトレンドが「横ばい傾向」から「インフレ加速傾向」へ変化しました。" in changes
    assert "雇用状況が「雇用横ばい」から「雇用改善」へ変化しました。" in changes
    assert "総合スコアが 0 から 5 へ変化しました。" in changes
    assert "総合分析が「中立景気」から「好景気」へ変化しました。" in changes

def test_detect_economic_changes_when_no_previous_result(tmp_path, monkeypatch):
    test_file = tmp_path / "analysis_history.csv"

    monkeypatch.setattr(history, "HISTORY_FILE", str(test_file))

    changes = history.detect_economic_changes(
        "インフレ",
        "インフレ加速傾向",
        "雇用改善",
        "雇用改善傾向",
        "金融引き締め",
        5,
        "好景気"
    )

    assert changes == []
    
    

# ----------概要----------
# 1.分析結果をCSVに保存できる
# 2.保存した最新結果を取得できる
# 3.履歴ファイルが存在しない場合
# 4.空の履歴ファイルの場合
# 5.前回結果との比較
# 6.経済状態の変化検出
# 7.前回結果がない場合の変化検出