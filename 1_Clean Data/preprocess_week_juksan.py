import pandas as pd
import os


def add_yield(filename, window):

    df = pd.read_csv(filename)

    sslist = []
    for i in range(window):
        ds = df.filter(regex=f'단위면적당생산량_{i+1}')
        for j in range(len(ds)):
            sslist.append(ds.iloc[j].values)

    sinlist = []
    for s in range(len(sslist)):
        sinlist.append(sslist[s][0])

    value = []
    for d in range(window):
        length = len(df)
        value.append(list(sinlist[d*length:length*(d+1)]))

    sumlist = []
    for m in range(len(value[0])):
        sum = 0
        for z in range(window):
            sum = sum + value[z][m]
        sumlist.append(sum)

    df.insert(len(df.columns), '누적단위면적당생산량', sumlist)

    for x in range(window):
        del df[f'단위면적당생산량_{x+1}']

    return df


def main():
    window = 4
    output_dir = f"../Output/Data/Farm_Color/Week{window}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file = ['Orange_0.csv', 'Orange_1.csv',
            'Red_1.csv', 'Red_2.csv', 'Red_3.csv', 'Red_4.csv', 'Red_5.csv',
            'Yellow_1.csv', 'Yellow_2.csv', 'Yellow_3.csv', 'Yellow_4.csv', 'Yellow_5.csv']

    for f in file:
        filename = f"../Output/Week{window}/{f}"
        data = add_yield(filename, window)
        output_filename = os.path.join(output_dir, "{}".format(f))
        data.to_csv(output_filename, index=False, encoding="utf-8-sig")


if __name__ == '__main__':
    main()