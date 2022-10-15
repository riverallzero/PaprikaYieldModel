import preprocess_excel as ppe
import preprocess_csv as ppc
import preprocess_seperate as pps
import preprocess_week as ppw
import split_data as sd
import preprocess_firstyield_week as ppf
import preprocess_week_juksan as pwj
import merge_color as mc
import os


# 1. preprocess_excel.py
filename = "../Input/파프리카 농가 생산량 알고리즘 개발 자료(동계작형_정리본).xlsx"

preprocess1 = ppe.read_data(filename)
output_dir = "../Output/Data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_filename = os.path.join(output_dir, "paprika_data.csv")
preprocess1.to_csv(output_filename, index=False, encoding="utf-8-sig")

# 2. preprocess_csv.py
filename = "../Output/Data/paprika_data.csv"

preprocess2 = ppc.convert_data(filename)
output_dir = "../Output/Data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

preprocess2 = preprocess2.dropna()
output_filename = os.path.join(output_dir, "paprika_winter.csv")
preprocess2.to_csv(output_filename, index=False, encoding="utf-8-sig")

# 3. preprocess_seperate.py
filename = "../Output/Data/paprika_winter.csv"

output_dir = "../Output/Data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

preprocess3 = pps.read_csv(filename)
colorname = ['paprika(Yellow).csv', 'paprika(Red).csv', 'paprika(Orange).csv']

for i in range(len(colorname)):
    output_filename = os.path.join(output_dir, colorname[i])
    preprocess3[i].to_csv(output_filename, index=False, encoding="utf-8-sig")

# 4. preprocess_firstyield_week.py
output_dir = "../Output/Data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

filename = ["../Output/Data/paprika(Orange).csv", "../Output/Data/paprika(Red).csv", "../Output/Data/paprika(Yellow).csv"]

for i in filename:
    ppf.convert_week(i).to_csv(os.path.join(output_dir, i[15:]), index=False, encoding="utf-8-sig")

# 5. split_data.py

output_dir = "../Output/Data/Farm_Color"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

filename = ["../Output/Data/paprika(Orange).csv", "../Output/Data/paprika(Red).csv", "../Output/Data/paprika(Yellow).csv"]
for i in range(2):
    sd.split_orange(filename[0])[i].to_csv(os.path.join(output_dir, "Orange_{}.csv".format(i)), index=False, encoding="utf-8-sig")
for i in range(6):
    sd.split_red(filename[1])[i].to_csv(os.path.join(output_dir, "Red_{}.csv".format(i)), index=False, encoding="utf-8-sig")
for i in range(6):
    sd.split_yellow(filename[2])[i].to_csv(os.path.join(output_dir, "Yellow_{}.csv".format(i)), index=False, encoding="utf-8-sig")

# 몇 주간 데이터 설정
for window in range(4, 19):
    # 6. preprocess_week.py

    output_dir = f"../Output/Data/Week{window}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Orange
    file = ['Orange_0.csv', 'Orange_1.csv']

    for f in file:
        filename = "../Output/Data/Farm_Color/{}".format(f)

        output_filename = os.path.join(output_dir, "{}".format(f))

        df_o = ppw.read_orange(filename, window)
        df_o.to_csv(output_filename, index=False, encoding="utf-8-sig")

    # Red
    file = ['Red_1.csv', 'Red_2.csv', 'Red_3.csv', 'Red_4.csv', 'Red_5.csv']

    for f in file:
        filename = "../Output/Data/Farm_Color/{}".format(f)

        output_filename = os.path.join(output_dir, "{}".format(f))

        df_r = ppw.read_red(filename, window)
        df_r.to_csv(output_filename, index=False, encoding="utf-8-sig")

    # Yellow
    file = ['Yellow_1.csv', 'Yellow_2.csv', 'Yellow_3.csv', 'Yellow_4.csv', 'Yellow_5.csv']

    for f in file:
        filename = "../Output/Data/Farm_Color/{}".format(f)

        output_filename = os.path.join(output_dir, "{}".format(f))

        df_y = ppw.read_yellow(filename, window)
        df_y.to_csv(output_filename, index=False, encoding="utf-8-sig")


    # 7. preprocess_week_juksan.py

    output_dir = f"../Output/Data/Farm_Color/Week{window}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file = ['Orange_0.csv', 'Orange_1.csv',
            'Red_1.csv', 'Red_2.csv', 'Red_3.csv', 'Red_4.csv', 'Red_5.csv',
            'Yellow_1.csv', 'Yellow_2.csv', 'Yellow_3.csv', 'Yellow_4.csv', 'Yellow_5.csv']

    for f in file:
        filename = f"../Output/Data/Week{window}/{f}"
        data = pwj.add_yield(filename, window)
        output_filename = os.path.join(output_dir, "{}".format(f))
        data.to_csv(output_filename, index=False, encoding="utf-8-sig")


    # 8. merge_color.py
    output_dir = f"../Output/Data/FinalData/week{window}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data = mc.set_path(window)

    output_filename = os.path.join(output_dir, "paprika(Orange).csv")
    data[0].to_csv(output_filename, index=False, encoding="utf-8-sig")
    output_filename = os.path.join(output_dir, "paprika(Red).csv")
    data[1].to_csv(output_filename, index=False, encoding="utf-8-sig")
    output_filename = os.path.join(output_dir, "paprika(Yellow).csv")
    data[2].to_csv(output_filename, index=False, encoding="utf-8-sig")