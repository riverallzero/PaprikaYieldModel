import pandas as pd
import datetime
import os


def convert_data(filename):
    df = pd.read_csv(filename)
    df.loc[df['배액량'] != df['배액량'], '배액량'] = 0
    df.loc[df['스라브EC주사기'] != df['스라브EC주사기'], '스라브EC주사기'] = 0
    df.loc[df['스라브PH'] != df['스라브PH'], '스라브PH'] = 0
    df.loc[df['온실수확박스수'] != df['온실수확박스수'], '온실수확박스수'] = 0
    df.loc[df['온실총생산량'] != df['온실총생산량'], '온실총생산량'] = 0
    df.loc[df['단위면적당생산량'] != df['단위면적당생산량'], '단위면적당생산량'] = 0

    del df['주간CO2']
    del df['내부CO2']
    del df['단위면적당누적생산량']

    return pd.DataFrame(df)


def main():
    output_dir = "../Output/Data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = "../Output/Data/paprika_data.csv"

    data = convert_data(filename)
    data = data.dropna()
    output_filename = os.path.join(output_dir, "paprika_winter.csv")
    data.to_csv(output_filename, index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    main()