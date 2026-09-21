import csv
import os
from datetime import datetime


HISTORY_FILE = "data/analysis_history.csv"


def save_analysis_result(
    cpi_judgment,
    cpi_trend,
    employment_judgment,
    employment_trend,
    rate_judgment,
    score,
    overall_judgment
):
    os.makedirs("data", exist_ok=True)

    file_exists = os.path.exists(HISTORY_FILE)

    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "date",
                "cpi_judgment",
                "cpi_trend",
                "employment_judgment",
                "employment_trend",
                "rate_judgment",
                "score",
                "overall_judgment"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            cpi_judgment,
            cpi_trend,
            employment_judgment,
            employment_trend,
            rate_judgment,
            score,
            overall_judgment
        ])
        
def get_previous_result():
    if not os.path.exists(HISTORY_FILE):
        return None

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        return None

    return rows[-1]

def compare_with_previous(
    cpi_judgment,
    cpi_trend,
    employment_judgment,
    employment_trend,
    rate_judgment,
    score,
    overall_judgment
):
    previous = get_previous_result()

    if previous is None:
        print("比較可能な過去の分析結果がありません。")
        return

    print("\n--- 前回との比較 ---")

    if cpi_judgment != previous["cpi_judgment"]:
        print(
            f"CPI状況：{previous['cpi_judgment']} → {cpi_judgment}"
        )
    else:
        print(f"CPI状況：変化なし（{cpi_judgment}）")

    if cpi_trend != previous["cpi_trend"]:
        print(
            f"CPIトレンド：{previous['cpi_trend']} → {cpi_trend}"
        )
    else:
        print(f"CPIトレンド：変化なし（{cpi_trend}）")

    if employment_judgment != previous["employment_judgment"]:
        print(
            f"雇用状況：{previous['employment_judgment']} → {employment_judgment}"
        )
    else:
        print(f"雇用状況：変化なし（{employment_judgment}）")

    if employment_trend != previous["employment_trend"]:
        print(
            f"雇用トレンド：{previous['employment_trend']} → {employment_trend}"
        )
    else:
        print(f"雇用トレンド：変化なし（{employment_trend}）")

    if rate_judgment != previous["rate_judgment"]:
        print(
            f"金融政策：{previous['rate_judgment']} → {rate_judgment}"
        )
    else:
        print(f"金融政策：変化なし（{rate_judgment}）")

    if str(score) != previous["score"]:
        print(
            f"総合スコア：{previous['score']} → {score}"
        )
    else:
        print(f"総合スコア：変化なし（{score}）")

    if overall_judgment != previous["overall_judgment"]:
        print(
            f"総合分析：{previous['overall_judgment']} → {overall_judgment}"
        )
    else:
        print(f"総合分析：変化なし（{overall_judgment}）")
        
def detect_economic_changes(
    cpi_judgment,
    cpi_trend,
    employment_judgment,
    employment_trend,
    rate_judgment,
    score,
    overall_judgment
):
    previous = get_previous_result()

    if previous is None:
        print("\n--- 経済状態の変化検出 ---")
        print("比較可能な過去の分析結果がありません。")
        return []

    changes = []

    # CPIの変化
    if cpi_judgment != previous["cpi_judgment"]:
        changes.append(
            f"CPI状況が「{previous['cpi_judgment']}」から"
            f"「{cpi_judgment}」へ変化しました。"
        )

    if cpi_trend != previous["cpi_trend"]:
        changes.append(
            f"CPIトレンドが「{previous['cpi_trend']}」から"
            f"「{cpi_trend}」へ変化しました。"
        )

    # 雇用の変化
    if employment_judgment != previous["employment_judgment"]:
        changes.append(
            f"雇用状況が「{previous['employment_judgment']}」から"
            f"「{employment_judgment}」へ変化しました。"
        )

    if employment_trend != previous["employment_trend"]:
        changes.append(
            f"雇用トレンドが「{previous['employment_trend']}」から"
            f"「{employment_trend}」へ変化しました。"
        )

    # 金融政策の変化
    if rate_judgment != previous["rate_judgment"]:
        changes.append(
            f"金融政策が「{previous['rate_judgment']}」から"
            f"「{rate_judgment}」へ変化しました。"
        )

    # 総合スコアの変化
    previous_score = int(previous["score"])

    if score != previous_score:
        changes.append(
            f"総合スコアが {previous_score} から {score} へ変化しました。"
        )

    # 総合判断の変化
    if overall_judgment != previous["overall_judgment"]:
        changes.append(
            f"総合分析が「{previous['overall_judgment']}」から"
            f"「{overall_judgment}」へ変化しました。"
        )

    print("\n--- 経済状態の変化検出 ---")

    if not changes:
        print("前回から経済状態に大きな変化はありません。")
    else:
        for change in changes:
            print(f"・{change}")

    return changes