import pandas as pd
import os


def set_window(df, window):

    row = len(df)
    index_num = []
    for i in range(0, row - (window - 1)):
        index_num.append(i)

    df_list = []
    for i in range(window):
        d1 = df.iloc[i:]
        for j in range(window - (i + 1)):
            d1 = d1.drop(d1.index[-1])
        d1.index = index_num
        df_list.append(d1)

    df_renamed_list = []
    for i, d1 in enumerate(df_list):
        d1 = add_postfix(d1, "_{}".format(i + 1))
        df_renamed_list.append(d1)

    result = pd.concat(df_renamed_list, axis=1)

    return result


def add_postfix(df, postfix):
    df = df.copy()
    for column_name in df.columns:
        df.rename(columns={column_name: column_name + postfix}, inplace=True)
    return df


def read_orange(filename: str, window) -> None:
    df = pd.read_csv(filename)
    ro = set_window(df, window)

    return ro


def read_red(filename: str, window) -> None:
    if filename[-5:-4] == "0":
        df = pd.read_csv(filename)[3:]
        rr = set_window(df, window)

    elif filename[-5:-4] == "1" or filename[-5:-4] == "2" or filename[-5:-4] == "3" or filename[-5:-4] == "4" or filename[-5:-4] == "5":
        df = pd.read_csv(filename)
        rr = set_window(df, window)

    return rr


def read_yellow(filename: str, window) -> None:
    if filename[-5:-4] == "0":
        df = pd.read_csv(filename)[3:]
        ry = set_window(df, window)

    elif filename[-5:-4] == "1" or filename[-5:-4] == "2" or filename[-5:-4] == "3" or filename[-5:-4] == "4" or filename[-5:-4] == "5":
        df = pd.read_csv(filename)
        ry = set_window(df, window)

    return ry


def main():
    window = 4
    output_dir = f"../Output/Data/Week{window}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Orange
    file = ['Orange_0.csv', 'Orange_1.csv']

    for f in file:
        filename = "../Output/Data/Farm_Color/{}".format(f)

        output_filename = os.path.join(output_dir, "{}".format(f))

        df_o = read_orange(filename, window)
        df_o.to_csv(output_filename, index=False, encoding="utf-8-sig")

    # Red
    file = ['Red_1.csv', 'Red_2.csv', 'Red_3.csv', 'Red_4.csv', 'Red_5.csv']

    for f in file:
        filename = "../Output/Data/Farm_Color/{}".format(f)

        output_filename = os.path.join(output_dir, "{}".format(f))

        df_r = read_red(filename, window)
        df_r.to_csv(output_filename, index=False, encoding="utf-8-sig")

    # Yellow
    file = ['Yellow_1.csv', 'Yellow_2.csv', 'Yellow_3.csv', 'Yellow_4.csv', 'Yellow_5.csv']

    for f in file:
        filename = "../Output/Data/Farm_Color/{}".format(f)

        output_filename = os.path.join(output_dir, "{}".format(f))

        df_y = read_yellow(filename, window)
        df_y.to_csv(output_filename, index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    main()