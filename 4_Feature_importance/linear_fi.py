import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import math


def main():
    filelist = [r"C:\Code\Paprika_model-main\Output\Result\linear\적색계_linear_importance.csv",
                r"C:\Code\Paprika_model-main\Output\Result\linear\황색계_linear_importance.csv",
                r"C:\Code\Paprika_model-main\Output\Result\linear\주황색계_linear_importance.csv"
                ]

    dataset = []
    dataset2 = []
    for file in filelist:
        df = pd.read_csv(file)

        df["coef*std"] = [abs(x) for x in df["coef*std"]]

        if "적" in file:
            cul = "적색계"
        elif "주" in file:
            cul = "주황색계"
        else:
            cul = "황색계"

        items = ["스라브PH", "스라브EC주사기", "배액량", "공급총량", "드리퍼당공급량", "작물흡수량", "광량당수분공급량", "공급횟수"]
        t_items = ["내부24시간평균온도", "내부야간평균온도", "내부주간평균온도"]
        h_items = ["내부24간평균HD", "내부야간평균HD", "내부주간평균HD"]

        growths_items = []
        t_s = []
        h_s = []

        for d in range(1, 18):
            for i in items:
                growths_items.append(f"{i}_{d}")
            for i in t_items:
                t_s.append(f"{i}_{d}")
            for i in h_items:
                h_s.append(f"{i}_{d}")

        item_class = []
        for data in df["item"]:
            if data not in growths_items:
                item_class.append("Environment")
            else:
                item_class.append("Growth")
        df["class"] = item_class

        fi = df.groupby(df["class"])["coef*std"].sum()
        dataset.append({
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
        fi_2 = df_2.groupby(df_2["class"])["coef*std"].sum()
        dataset2.append({
            "Cultivar": cul,
            "Temperature": fi_2[0],
            "Humid": fi_2[1],
            "Sunset": fi_2[2]
        })

    dataset = pd.DataFrame(dataset)
    dataset2 = pd.DataFrame(dataset2)

    # 변수중요도 그리기
    size = 18
    params = {
        'axes.labelsize': size * 1.1,
        'axes.titlesize': size * 1.2,
        'xtick.labelsize': size,
        'ytick.labelsize': size,
    }
    plt.rcParams.update(params)

    labels = dataset["Cultivar"]
    plt.figure(figsize=(5, 3.5))

    # # 1. 환경, 생육 데이터
    # plt.bar(labels, dataset["Environment"], label='Environment', color="orange")
    # plt.bar(labels, dataset["Growth"], bottom=dataset["Environment"], label='Growth', color="yellowgreen")
    # plt.legend(loc="upper right")
    #
    # plt.title("Linear Regression")
    # plt.tight_layout()
    # plt.savefig("Linear_feature1.png", dpi=600)

    # 2. 환경 데이터 안에서 비교
    plt.bar(labels, dataset2["Sunset"], label='Sunset', color="gold")
    plt.bar(labels, dataset2["Humid"], bottom=dataset2["Sunset"], label='Humid', color="lightseagreen")
    plt.bar(labels, dataset2["Temperature"], bottom=dataset2["Sunset"], label='Temperature', color="indianred")

    plt.legend(loc="lower right")
    plt.title("Environment")
    plt.tight_layout()
    plt.savefig("Linear_feature2.png", dpi=600)
    plt.show()


if __name__ == "__main__":
    main()