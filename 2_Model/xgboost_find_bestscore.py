import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from tqdm import tqdm
import os


def fine_score(filename, window):
    df = pd.read_csv(filename)
    y = df['누적단위면적당생산량']

    exclude_list = []
    for col_name in df.columns:
        for field in ["농가", "품종", "색상", "면적", "온실종류", "온실수확박스수", "온실총생산량",  "정식일자", "첫생산일기준주차", "정식기준주차", "date", "year", "month", "day"]:
            if col_name.startswith(field):
                exclude_list.append(col_name)

    for e in exclude_list:
        del df[e]

    X = df.drop(['누적단위면적당생산량'], axis=1).select_dtypes(exclude=['object'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.6, random_state=777)

    model = XGBRegressor()

    model.fit(X_train, y_train)

    y_predict = model.predict(X_test)

    r2 = r2_score(y_predict, y_test)
    mae = mean_absolute_error(y_predict, y_test)

    if 'Orange' in filename:
        cul = 'orange'
    elif 'Red' in filename:
        cul = 'red'
    elif 'Yellow' in filename:
        cul = 'yellow'
    dataset = []

    dataset.append({
        'Week': window,
        'Cultivars': cul,
        'R2S': "{:.2f}".format(r2),
        'MAE': "{:.2f}".format(mae)
    })

    return pd.DataFrame(dataset)


def main():
    output_dir = "../Output/Result"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = ["paprika(Orange).csv", "paprika(Red).csv", "paprika(Yellow).csv"]

    data = []

    for window in tqdm(range(4, 19)):
        for f in filename:
            result = fine_score(f"../Output/Data/FinalData/Week{window}/{f}", window)
            data.append(result)

    result = pd.concat(data, axis=0, ignore_index=True)

    output_filename = os.path.join(output_dir, "xgb_result.csv")
    result.to_csv(output_filename, index=False, encoding="utf-8-sig")


if __name__ == '__main__':
    main()