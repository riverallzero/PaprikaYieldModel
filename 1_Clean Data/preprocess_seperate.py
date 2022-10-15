import pandas as pd
import os


def read_csv(filename):
    df = pd.read_csv(filename)
    df_yellow = df[(df['색상'] == 'YELLOW')]
    df_red = df[(df['색상'] == 'RED')]
    df_orange = df[(df['색상'] == 'ORANGE')]

    return df_yellow, df_red, df_orange


def main():
    output_dir = "../Output/Data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = "../Output/Data/paprika_winter.csv"

    colorname = ['paprika(Yellow).csv', 'paprika(Red).csv', 'paprika(Orange).csv']

    for i in range(len(colorname)):
        output_filename = os.path.join(output_dir, colorname[i])
        read_csv(filename)[i].to_csv(output_filename, index=False, encoding="utf-8-sig")


if __name__ == '__main__':
    main()
