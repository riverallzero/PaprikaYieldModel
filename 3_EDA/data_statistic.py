import pandas as pd
import os


def main():
    output_dir = "../Output/Table"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df_red = pd.read_csv("../Output/Data/paprika(Red).csv")
    red_table = df_red.describe()
    df_yellow = pd.read_csv("../Output/Data/paprika(Yellow).csv")
    yellow_table = df_yellow.describe()
    df_orange = pd.read_csv("../Output/Data/paprika(Orange).csv")
    orange_table = df_orange.describe()

    items = ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]
    red_table.insert(0, "item", items)
    yellow_table.insert(0, "item", items)
    orange_table.insert(0, "item", items)

    red_table.to_csv(os.path.join(output_dir, "Red.csv"), index=False, encoding="utf-8-sig")
    yellow_table.to_csv(os.path.join(output_dir, "Yellow.csv"), index=False, encoding="utf-8-sig")
    orange_table.to_csv(os.path.join(output_dir, "Orange.csv"), index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    main()