def generate_report(
    cpi_judgment,
    cpi_trend,
    employment_judgment,
    employment_trend,
    rate_judgment,
    score,
    overall_judgment,
    changes
):
    print("\n========== 経済分析レポート ==========")


    # 総合評価
    print("\n【総合評価】")
    print(f"総合スコア：{score}")
    print(f"総合分析：{overall_judgment}")


    # CPI分析
    print("\n【CPI分析】")
    print(f"CPI状況：{cpi_judgment}")
    print(f"CPIトレンド：{cpi_trend}")

    if cpi_judgment == "インフレ":
        if "鈍化" in cpi_trend:
            cpi_comment = (
                "インフレ状態にあるものの、インフレ圧力には鈍化傾向が見られます。"
            )
        else:
            cpi_comment = (
                "インフレ状態にあり、インフレ圧力が継続している可能性があります。"
            )

    elif cpi_judgment == "ディスインフレ":
        cpi_comment = (
            "インフレは低下しており、インフレ圧力が弱まっている可能性があります。"
        )

    else:
        cpi_comment = (
            "物価は比較的安定した状態にあります。"
        )

    print(f"分析：{cpi_comment}")


    # 雇用分析
    print("\n【雇用分析】")
    print(f"雇用状況：{employment_judgment}")
    print(f"雇用トレンド：{employment_trend}")

    if employment_judgment == "雇用改善":
        if "横ばい" in employment_trend:
            employment_comment = (
                "雇用は改善しているものの、足元では大きな変化が見られず、横ばい傾向にあります。"
            )
        else:
            employment_comment = (
                "雇用は改善しており、労働市場は比較的堅調な状態にあります。"
            )

    elif employment_judgment == "雇用悪化":
        employment_comment = (
            "雇用には悪化傾向が見られ、労働市場の弱含みに注意が必要です。"
        )

    else:
        employment_comment = (
            "雇用環境について明確な判断はできません。"
        )

    print(f"分析：{employment_comment}")


    # 金融政策分析
    print("\n【金融政策分析】")
    print(f"金融政策：{rate_judgment}")

    if rate_judgment == "高金利":
        rate_comment = (
            "金融政策は引き締め的な水準にあり、景気や物価に対して抑制的に作用する可能性があります。"
        )

    elif rate_judgment == "低金利":
        rate_comment = (
            "金融政策は緩和的な水準にあり、景気を下支えする方向に作用する可能性があります。"
        )

    elif rate_judgment == "金融政策中立":
        rate_comment = (
            "金融政策は中立的な状態にあり、現時点では金融政策による景気への方向性は確認されません。"
        )

    else:
        rate_comment = (
            "金融政策について明確な判断はできません。"
        )

    print(f"分析：{rate_comment}")


    # 指標間の総合分析
    print("\n【総合分析】")

    if overall_judgment == "景気拡大":
        overall_comment = (
            "物価、雇用、金融政策の状況を総括すると、景気は拡大基調にあると判断されます。"
        )

    elif overall_judgment == "景気後退":
        overall_comment = (
            "物価、雇用、金融政策の状況を総合すると、景気は縮小基調にあると判断されます。"
        )

    elif overall_judgment == "中立景気":
        overall_comment = (
            "物価、雇用、金融政策を総合すると、景気は中立的な状態にあると判断されます。"
        )

    else:
        overall_comment = (
            "複数の経済指標を総合した結果、明確な景気方向は確認されませんでした。。"
        )

    print(f"分析：{overall_comment}")


    # 指標間の関係
    print("\n【指標間の関係】")

    if (
        cpi_judgment == "インフレ"
        and employment_judgment == "雇用改善"
    ):
        relationship_comment = (
            "インフレと雇用改善が同時に確認されており、経済が強含んでいる傾向があります。"
        )

    elif (
        cpi_judgment == "ディスインフレ"
        and employment_judgment == "雇用悪化"
    ):
        relationship_comment = (
            "ディスインフレと雇用悪化が同時に確認されており、経済の弱含みに注意が必要な状況です。"
        )

    elif employment_judgment == "雇用改善":
        relationship_comment = (
            "雇用は改善しており、景気を下支えする要因となっている可能性があります。"
        )

    elif employment_judgment == "雇用悪化":
        relationship_comment = (
            "雇用の悪化が確認されており、景気の下押し要因となる可能性があります。"
        )

    else:
        relationship_comment = (
            "各指標の間に明確な方向性は確認されませんでした。"
        )

    print(f"分析：{relationship_comment}")


    # 前回からの変化
    print("\n【前回からの変化】")

    if not changes:
        print("前回から大きな変化はありません。")
    else:
        for change in changes:
            print(f"・{change}")

    print("\n======================================")