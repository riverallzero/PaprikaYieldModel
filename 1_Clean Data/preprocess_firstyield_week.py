import pandas as pd
import os
import datetime


def convert_week(filename):
    df = pd.read_csv(filename)

    if filename == "../Output/Data/paprika(Orange).csv":
        farmname = ['성현영농조합법인', '해담토']

        year = []
        month = []
        day = []

        dyear = []
        dmonth = []
        dday = []

        year.append(list(df['year']))
        month.append(list(df['month']))
        day.append(list(df['day']))

        for c in df['date']:
            dyear.append(int(c.split('-')[0]))
            dmonth.append(int(c.split('-')[1]))
            dday.append(int(c.split('-')[2][:2]))


        farmlen = []
        for f in farmname:
            farmlen.append(len(df[df['농가'] == f]))

        weeks = []
        for f in range(farmlen[0]):
            weeks.append((datetime.date(dyear[f], dmonth[f], dday[f]) - datetime.date(dyear[0], dmonth[0], dday[0])).days//7)
        for f in range(farmlen[0], farmlen[0]+farmlen[1]):
            weeks.append((datetime.date(dyear[f], dmonth[f], dday[f]) - datetime.date(dyear[farmlen[0]], dmonth[farmlen[0]], dday[farmlen[0]])).days//7)

        df.insert(10, '첫생산일기준주차', weeks)

    elif filename == "../Output/Data/paprika(Red).csv":
        farmname = ['김제애농영농조합법인', '성현영농조합법인', '아현영농조합법인', '유연영농조합법인', '참샘D', '해담토']

        year = []
        month = []
        day = []

        dyear = []
        dmonth = []
        dday = []

        year.append(list(df['year']))
        month.append(list(df['month']))
        day.append(list(df['day']))

        for c in df['date']:
            dyear.append(int(c.split('-')[0]))
            dmonth.append(int(c.split('-')[1]))
            dday.append(int(c.split('-')[2][:2]))

        farmlen = []
        for f in farmname:
            farmlen.append(len(df[df['농가'] == f]))

        weeks = []
        for f in range(farmlen[0]):
            weeks.append(
                (datetime.date(dyear[f], dmonth[f], dday[f]) - datetime.date(dyear[0], dmonth[0], dday[0])).days // 7)

        for f in range(farmlen[0], farmlen[0]+farmlen[1]):
            weeks.append(
                (datetime.date(dyear[f], dmonth[f], dday[f]) - datetime.date(dyear[farmlen[0]], dmonth[farmlen[0]], dday[farmlen[0]])).days // 7)

        for f in range(farmlen[0]+farmlen[1], farmlen[0]+farmlen[1]+farmlen[2]):
            weeks.append(
                (datetime.date(dyear[f], dmonth[f], dday[f]) - datetime.date(dyear[farmlen[0]+farmlen[1]], dmonth[farmlen[0]+farmlen[1]], dday[farmlen[0]+farmlen[1]])).days // 7)

        for f in range(farmlen[0]+farmlen[1]+farmlen[2], farmlen[0]+farmlen[1]+farmlen[2]+farmlen[3]):
            weeks.append(
                (datetime.date(dyear[f], dmonth[f], dday[f]) - datetime.date(dyear[farmlen[0]+farmlen[1]+farmlen[2]], dmonth[farmlen[0]+farmlen[1]+farmlen[2]], dday[farmlen[0]+farmlen[1]+farmlen[2]])).days // 7)

        for f in range(farmlen[0]+farmlen[1]+farmlen[2]+farmlen[3], farmlen[0]+farmlen[1]+farmlen[2]+farmlen[3]+farmlen[4]):
            weeks.append(
                (datetime.date(dyear[f], dmonth[f], dday[f]) - datetime.date(dyear[farmlen[0]+farmlen[1]+farmlen[2]+farmlen[3]], dmonth[farmlen[0]+farmlen[1]+farmlen[2]+farmlen[3]], dday[farmlen[0]+farmlen[1]+farmlen[2]+farmlen[3]])).days // 7)

        for f in range(farmlen[0]+farmlen[1]+farmlen[2]+farmlen[3]+farmlen[4], farmlen[0]+farmlen[1]+farmlen[2]+farmlen[3]+farmlen[4]+farmlen[5]):
            weeks.append(
                (datetime.date(dyear[f], dmonth[f], dday[f]) - datetime.date(dyear[farmlen[0]+farmlen[1]+farmlen[2]+farmlen[3]+farmlen[4]], dmonth[farmlen[0]+farmlen[1]+farmlen[2]+farmlen[3]+farmlen[4]], dday[farmlen[0]+farmlen[1]+farmlen[2]+farmlen[3]+farmlen[4]])).days // 7)

        df.insert(10, '첫생산일기준주차', weeks)

    elif filename == "../Output/Data/paprika(Yellow).csv":
        farmname = ['김제애농영농조합법인', '염산김민환', '유연영농조합법인', '진현농장', '참샘영농조합법인', '해담토']

        year = []
        month = []
        day = []

        dyear = []
        dmonth = []
        dday = []

        year.append(list(df['year']))
        month.append(list(df['month']))
        day.append(list(df['day']))

        for c in df['date']:
            dyear.append(int(c.split('-')[0]))
            dmonth.append(int(c.split('-')[1]))
            dday.append(int(c.split('-')[2][:2]))

        farmlen = []
        for f in farmname:
            farmlen.append(len(df[df['농가'] == f]))

        weeks = []

        for f in range(farmlen[0]):
            weeks.append(
                (datetime.date(dyear[f], dmonth[f], dday[f]) - datetime.date(dyear[0], dmonth[0], dday[0])).days // 7)
        for f in range(farmlen[0], farmlen[0] + farmlen[1]):
            weeks.append(
                (datetime.date(dyear[f], dmonth[f], dday[f]) - datetime.date(dyear[farmlen[0]], dmonth[farmlen[0]], dday[farmlen[0]])).days // 7)
        for f in range(farmlen[0] + farmlen[1], farmlen[0] + farmlen[1] + farmlen[2]):
            weeks.append(
                (datetime.date(dyear[f], dmonth[f], dday[f]) - datetime.date(dyear[farmlen[0] + farmlen[1]], dmonth[farmlen[0] + farmlen[1]], dday[farmlen[0] + farmlen[1]])).days // 7)
        for f in range(farmlen[0] + farmlen[1] + farmlen[2], farmlen[0] + farmlen[1] + farmlen[2] + farmlen[3]):
            weeks.append(
                (datetime.date(dyear[f], dmonth[f], dday[f]) - datetime.date(dyear[farmlen[0] + farmlen[1] + farmlen[2]], dmonth[farmlen[0] + farmlen[1] + farmlen[2]], dday[farmlen[0] + farmlen[1] + farmlen[2]])).days // 7)
        for f in range(farmlen[0] + farmlen[1] + farmlen[2] + farmlen[3], farmlen[0] + farmlen[1] + farmlen[2] + farmlen[3] + farmlen[4]):
            weeks.append(
                (datetime.date(dyear[f], dmonth[f], dday[f]) - datetime.date(dyear[farmlen[0] + farmlen[1] + farmlen[2] + farmlen[3]], dmonth[farmlen[0] + farmlen[1] + farmlen[2] + farmlen[3]], dday[farmlen[0] + farmlen[1] + farmlen[2] + farmlen[3]])).days // 7)
        for f in range(farmlen[0] + farmlen[1] + farmlen[2] + farmlen[3] + farmlen[4], farmlen[0] + farmlen[1] + farmlen[2] + farmlen[3] + farmlen[4] + farmlen[5]):
            weeks.append(
                (datetime.date(dyear[f], dmonth[f], dday[f]) - datetime.date(dyear[farmlen[0] + farmlen[1] + farmlen[2] + farmlen[3] + farmlen[4]], dmonth[farmlen[0] + farmlen[1] + farmlen[2] + farmlen[3] + farmlen[4]], dday[farmlen[0] + farmlen[1] + farmlen[2] + farmlen[3] + farmlen[4]])).days // 7)

        df.insert(10, '첫생산일기준주차', weeks)

    return df

def main():
    output_dir = "../Output/Data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = ["../Output/Data/paprika(Orange).csv", "../Output/Data/paprika(Red).csv", "../Output/Data/paprika(Yellow).csv"]

    for i in filename:
        convert_week(i).to_csv(os.path.join(output_dir, i[15:]), index=False, encoding="utf-8-sig")


if __name__ == '__main__':
    main()