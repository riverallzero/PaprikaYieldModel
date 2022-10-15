import pandas as pd
import os


def split_orange(filename):
    df = pd.read_csv(filename)

    ds1 = df[(df['농가'] == '성현영농조합법인')]
    ds2 = df[(df['농가'] == '해담토')]

    return ds1, ds2


def split_red(filename):
    df = pd.read_csv(filename)

    ds3 = df[(df['농가'] == '김제애농영농조합법인')]
    ds4 = df[(df['농가'] == '성현영농조합법인')]
    ds5 = df[(df['농가'] == '아현영농조합법인')]
    ds6 = df[(df['농가'] == '유연영농조합법인')]
    ds7 = df[(df['농가'] == '참샘D')]
    ds8 = df[(df['농가'] == '해담토')]

    return ds3, ds4, ds5, ds6, ds7, ds8


def split_yellow(filename):
    df = pd.read_csv(filename)

    ds9 = df[(df['농가'] == '김제애농영농조합법인')]
    ds10 = df[(df['농가'] == '염산김민환')]
    ds11 = df[(df['농가'] == '유연영농조합법인')]
    ds12 = df[(df['농가'] == '진현농장')]
    ds13 = df[(df['농가'] == '참샘영농조합법인')]
    ds14 = df[(df['농가'] == '해담토')]

    return ds9, ds10, ds11, ds12, ds13, ds14


def main():
    output_dir = "../Output/Data/Farm_Color"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = ["../Output/Data/paprika(Orange).csv", "../Output/Data/paprika(Red).csv", "../Output/Data/paprika(Yellow).csv"]
    for i in range(2):
        split_orange(filename[0])[i].to_csv(os.path.join(output_dir, "Orange_{}.csv".format(i)), index=False, encoding="utf-8-sig")
    for i in range(6):
        split_red(filename[1])[i].to_csv(os.path.join(output_dir, "Red_{}.csv".format(i)), index=False, encoding="utf-8-sig")
    for i in range(6):
        split_yellow(filename[2])[i].to_csv(os.path.join(output_dir, "Yellow_{}.csv".format(i)), index=False, encoding="utf-8-sig")


if __name__ == '__main__':
    main()