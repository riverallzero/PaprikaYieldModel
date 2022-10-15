import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib import font_manager, rc
import platform

if platform.system() == "Darwin":
    plt.rc('font', family='AppleGothic')
elif platform.system() == "Windows":
    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)


def main():
    output_dir = "../Output/Figures"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df_red = pd.read_csv("../Output/Data/paprika(Red).csv")
    df_orange = pd.read_csv("../Output/Data/paprika(Orange).csv")
    df_yellow = pd.read_csv("../Output/Data/paprika(Yellow).csv")

    size = 18
    params = {
        'axes.labelsize': size * 0.8,
        'axes.titlesize': size * 1.2,
    }
    plt.rcParams.update(params)

    fig, ax = plt.subplots(ncols=3, figsize=(15, 6), sharey=True)

    x1 = df_red["농가"]
    y1 = df_red["단위면적당생산량"]
    x2 = df_yellow["농가"]
    y2 = df_yellow["단위면적당생산량"]
    x3 = df_orange["농가"]
    y3 = df_orange["단위면적당생산량"]

    g1 = sns.stripplot(x=x1, y=y1, ax=ax[0])
    g1.set_title("적색계")
    g2 = sns.stripplot(x=x2, y=y2, ax=ax[1])
    g2.set_title("황색계")
    g3 = sns.stripplot(x=x3, y=y3, ax=ax[2])
    g3.set_title("주황색계")

    g2.set_ylabel("")
    g3.set_ylabel("")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "data_plot.png"), dpi=600)
    plt.show()


if __name__ == "__main__":
    main()