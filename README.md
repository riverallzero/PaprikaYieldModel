# XGBoost 기반 중요 주간 판별을 통한 파프리카 품종별 생산량 예측 모델

## 설명
- 2022 추계 원예학회 학술발표 in 제주국제컨벤션센터(11/02~05) 
- 이용 기술 : pandas, scikit-learn, matplotlib, seaborn
- 데이터 보안을 위해 Input 폴더 삭제

## 코드 설명
### 1_Clean Data
모델링을 위한 데이터 전처리 과정
-  <strong>전처리 전과정 수행 | <a href="https://github.com/riverallzero/Paprika_model/blob/main/1_Clean%20Data/preprocess_all.py">preprocess_all.py</a></strong> 
    * <a href="https://github.com/riverallzero/Paprika_model/blob/main/1_Clean%20Data/preprocess_excel.py">preprocess_excel.py</a>
  : 받아온 생육조사데이터 엑셀파일을 데이터프레임의 csv 형식으로 변환
    * <a href="https://github.com/riverallzero/Paprika_model/blob/main/1_Clean%20Data/preprocess_csv.py">preprocess_csv.py</a>
  : 데이터 결측치 제거 및 보완
    * <a href="https://github.com/riverallzero/Paprika_model/blob/main/1_Clean%20Data/preprocess_seperate.py">preprocess_seperate.py</a>
  : 파프리카 품종별(적색계, 황색계, 주황색계) 데이터 분리
    * <a href="https://github.com/riverallzero/Paprika_model/blob/main/1_Clean%20Data/preprocess_firstyield_week.py">preprocess_firstyield_week.py</a>
  : 첫 생산일 기준 주차 열 추가
    * <a href="https://github.com/riverallzero/Paprika_model/blob/main/1_Clean%20Data/split_data.py">split_data.py</a>
  : 품종기준 농가별 데이터 분리
    * <a href="https://github.com/riverallzero/Paprika_model/blob/main/1_Clean%20Data/preprocess_week_juksan.py">preprocess_week_juksan.py</a>
  : window별로 feature를 옆으로 붙이는 과정(window 는 주차의 누적으로 window가 4일때 4주차의 데이터로 5주차의 생산량을 예측한다는 의미)
    * <a href="https://github.com/riverallzero/Paprika_model/blob/main/1_Clean%20Data/merge_color.py">merge_color.py</a>
  : 품종기준 농가별 분리한 데이터 합치기
  
### 2_Model
XGBoost, Linear Regression를 이용한 최적 주차 선정 및 모델링
- 최적 주차 선정
    * XGBoost
    <img src="https://user-images.githubusercontent.com/93754504/197727972-f98759ff-6aad-46d9-b429-2c0a71a853bd.png" width="300px">
    
    * Linear Regression
    <img src="https://user-images.githubusercontent.com/93754504/197728154-dcf7de40-cc72-4911-ad79-9294271d599c.png" width="300px">

- 모델 결과 
  * <strong>XGBoost</strong> | <a href="https://github.com/riverallzero/Paprika_model/blob/main/2_Model/XGB_model.py">XGB_model.py</a>
  <img src="https://user-images.githubusercontent.com/93754504/198185825-5596b138-585b-4135-bb7c-a660555c4d05.png" width="800px">

  * <strong>Linear Regression</strong> | <a href="https://github.com/riverallzero/Paprika_model/blob/main/2_Model/linear_model.py">linear_model.py</a>
  <img src="https://user-images.githubusercontent.com/93754504/198185872-c64c18c8-d954-499f-bf70-dae4f8db6bc8.png" width="800px">

### 3_EDA
- 품종기준 농가별 생산량 비교 stripplot
<img src="https://user-images.githubusercontent.com/93754504/197729489-bab245ed-9250-489f-898a-5fa7ba0aa2f2.png" width="800px">

### 4_Feature_importance
- 모델별 변수 중요도를 Stack형식 barplot(환경, 생육 데이터 분리해 비교)
<img src="https://user-images.githubusercontent.com/93754504/198185655-ce995b4a-5dcf-45ca-a01a-aa710533d8d9.png" width="800px">
<img src="https://user-images.githubusercontent.com/93754504/198185668-3b202f87-0408-4ad7-8379-82c3e48a70e9.png" width="800px">

## 결론
