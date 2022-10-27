import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


def main():
    filelist = [r"C:\Code\Paprika_model-main\Output\Result\xgb\적색계_xgb_importance.csv",
                r"C:\Code\Paprika_model-main\Output\Result\xgb\황색계_xgb_importance.csv",
                r"C:\Code\Paprika_model-main\Output\Result\xgb\주황색계_xgb_importance.csv"
    ]

    dataset1 = []
    dataset2 = []
    dataset3 = []
    for file in filelist:
        df = pd.read_csv(file)

        if "적" in file:
            cul = "적색계"
        elif "주" in file:
            cul = "주황색계"
        else:
            cul = "황색계"

        items = ["스라브PH", "스라브EC주사기", "배액량", "공급총량", "드리퍼당공급량", "작물흡수량", "광량당수분공급량", "공급횟수"]
        t_items = ["내부24시간평균온도", "내부야간평균온도", "내부주간평균온도"]
        h_items = ["내부24간평균HD", "내부야간평균HD", "내부주간평균HD"]
        # 양액공급관련
        g_items = ["1회공급량", "공급횟수", "드리퍼당공급량", "공급총량", "배액량", "스라브EC주사기", "스라브PH"]
        a_items = ["작물흡수량"]

        growths_items = []
        t_s = []
        h_s = []
        g_s = []
        a_s = []

        for d in range(1, 17):
            for i in items:
                growths_items.append(f"{i}_{d}")
            for i in t_items:
                t_s.append(f"{i}_{d}")
            for i in h_items:
                h_s.append(f"{i}_{d}")
            for i in g_items:
                g_s.append(f"{i}_{d}")
            for i in a_items:
                a_s.append(f"{i}_{d}")

        item_class = []
        for data in df["item"]:
            if data not in growths_items:
                item_class.append("Environment")
            else:
                item_class.append("Growth")
        df["class"] = item_class

        fi = df.groupby(df["class"])["feature_importance"].sum()
        dataset1.append({
            "Cultivar": cul,
            "Environment": fi[0],
            "Growth": fi[1]
        })

        # 환경데이터 분리
        df_2 = df[df["class"] == "Environment"].reset_index()
        del df_2["index"]
        item_class_2 = []
        for data in df_2["item"]:
            if data in t_s:
                item_class_2.append("Temperature")
            elif data in h_s:
                item_class_2.append("Humid")
            else:
                item_class_2.append("Sunset")
        df_2["class"] = item_class_2
        fi_2 = df_2.groupby(df_2["class"])["feature_importance"].sum()
        dataset2.append({
            "Cultivar": cul,
            "Temperature": fi_2[2],
            "Humid": fi_2[0],
            "Sunset": fi_2[1]
        })

        # 생육데이터 분리
        df_3 = df[df["class"] == "Growth"].reset_index()
        del df_3["index"]
        item_class_3 = []
        for data in df_3["item"]:
            if data in g_s:
                item_class_3.append("Nutrient-solution")
            elif data in a_s:
                item_class_3.append("Absorb")
            else:
                item_class_3.append("Water")
        df_3["class"] = item_class_3
        fi_3 = df_3.groupby(df_3["class"])["feature_importance"].sum()
        dataset3.append({
            "Cultivar": cul,
            "Nutrient-solution": fi_3[1],
            "Absorb": fi_3[0],
            "Water": fi_3[2]
        })

    dataset1 = pd.DataFrame(dataset1)
    dataset2 = pd.DataFrame(dataset2)
    dataset3 = pd.DataFrame(dataset3)

    # 변수중요도 그리기
    size = 18
    params = {
        'axes.labelsize': size * 1.1,
        'axes.titlesize': size * 1.2,
        'xtick.labelsize': size,
        'ytick.labelsize': size,
    }
    plt.rcParams.update(params)

    labels = dataset1["Cultivar"]
    plt.figure(figsize=(10, 3.5))
    plt.subplot(1, 3, 1)
    # 1. 환경, 생육 데이터
    plt.bar(labels, dataset1["Environment"], label='환경데이터', color="orange")
    plt.bar(labels, dataset1["Growth"], bottom=dataset1["Environment"], label='생육데이터', color="yellowgreen")
    plt.legend(loc="lower right")
    plt.title("XGBoost")

    plt.subplot(1, 3, 2)
    # 2. 환경 데이터 안에서 비교
    plt.bar(labels, dataset2["Sunset"], label='광량', color="gold")
    plt.bar(labels, dataset2["Temperature"], bottom=dataset2["Sunset"], label='온도', color="indianred")
    plt.bar(labels, dataset2["Humid"], bottom=dataset2["Sunset"], label='습도', color="lightseagreen")

    plt.legend(loc="lower right")
    plt.title("<Environment>")

    plt.subplot(1, 3, 3)
    # 3. 생육 데이터 안에서 비교
    plt.bar(labels, dataset3["Nutrient-solution"], label='양액관련항목', color="gold")
    plt.bar(labels, dataset3["Absorb"], bottom=dataset3["Nutrient-solution"], label='작물흡수량', color="indianred")
    plt.bar(labels, dataset3["Water"], bottom=dataset3["Nutrient-solution"], label='수분공급량', color="lightseagreen")

    plt.legend(loc="upper right")
    plt.title("<Growth>")

    plt.tight_layout()
    plt.savefig("XGBoost_feature.png", dpi=600)
    plt.show()


if __name__ == "__main__":
    main()