import pandas as pd
import os


def set_path(window):
    # set files path
    p_or0 = f'../Output/Data/Farm_Color/Week{window}/Orange_0.csv'
    p_or1 = f'../Output/Data/Farm_Color/Week{window}/Orange_1.csv'

    p_re1 = f'../Output/Data/Farm_Color/Week{window}/Red_1.csv'
    p_re2 = f'../Output/Data/Farm_Color/Week{window}/Red_2.csv'
    p_re3 = f'../Output/Data/Farm_Color/Week{window}/Red_3.csv'
    p_re4 = f'../Output/Data/Farm_Color/Week{window}/Red_4.csv'
    p_re5 = f'../Output/Data/Farm_Color/Week{window}/Red_5.csv'

    p_ye1 = f'../Output/Data/Farm_Color/Week{window}/Yellow_1.csv'
    p_ye2 = f'../Output/Data/Farm_Color/Week{window}/Yellow_2.csv'
    p_ye3 = f'../Output/Data/Farm_Color/Week{window}/Yellow_3.csv'
    p_ye4 = f'../Output/Data/Farm_Color/Week{window}/Yellow_4.csv'
    p_ye5 = f'../Output/Data/Farm_Color/Week{window}/Yellow_5.csv'


    # merge files
    dataFrame1 = pd.concat(
       map(pd.read_csv, [p_or0, p_or1]), ignore_index=True)

    dataFrame2 = pd.concat(
       map(pd.read_csv, [p_re1, p_re2, p_re3, p_re4, p_re5]), ignore_index=True)

    dataFrame3 = pd.concat(
       map(pd.read_csv, [p_ye1, p_ye2, p_ye3, p_ye4, p_ye5]), ignore_index=True)

    return dataFrame1, dataFrame2, dataFrame3


def main():
    window = 4

    output_dir = f"../Output/Data/FinalData/week{window}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data = set_path(window)

    output_filename = os.path.join(output_dir, "paprika(Orange).csv")
    data[0].to_csv(output_filename, index=False, encoding="utf-8-sig")
    output_filename = os.path.join(output_dir, "paprika(Red).csv")
    data[1].to_csv(output_filename, index=False, encoding="utf-8-sig")
    output_filename = os.path.join(output_dir, "paprika(Yellow).csv")
    data[2].to_csv(output_filename, index=False, encoding="utf-8-sig")


if __name__ == '__main__':
    main()