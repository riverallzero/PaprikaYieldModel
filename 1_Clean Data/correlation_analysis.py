import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import os
from matplotlib import font_manager, rc


font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


def draw_correlation(input_filename, output_filename, title="Red"):
    df = pd.read_csv(input_filename)

    corr = df.corr()
    fig, ax = plt.subplots(figsize=(30, 15))
    mask = np.triu(np.ones_like(corr, dtype=bool))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    sns.heatmap(corr, annot=True, mask=mask, cmap=cmap)
    # plt.savefig(output_filename)
    plt.show()


def main():
    output_dir = "../Output/CA(png)"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    input_filename1 = "../Output/Data/paprika(Red).csv"
    output_filename1 = os.path.join(output_dir, "Red.png")

    draw_correlation(input_filename1, output_filename1, title="Red")


if __name__ == '__main__':
    main()