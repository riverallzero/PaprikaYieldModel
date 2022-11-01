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
    <img src="https://user-images.githubusercontent.com/93754504/199156130-855b187e-8346-4a81-8dba-f23440db32a6.png" width="700px">

    * Linear Regression
    <img src="https://user-images.githubusercontent.com/93754504/199156139-96b04c3b-a239-42da-811b-7454c6c4ad52.png" width="700px">

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
<img src="https://user-images.githubusercontent.com/93754504/199156201-c596ead7-079b-46d8-9110-bbf7386ec422.png" width="800px">
<img src="https://user-images.githubusercontent.com/93754504/199156206-426125a3-d44a-4aea-9f9f-cb732d7f1ef6.png" width="800px">

## 결론
품종별 생산량 예측 모델의 최적주차를 살펴본 바, 3~4개월동안 주간 관측데이터를 활용한 모델이 가장 성능이 좋은 것을 확인했다. 최적주간을 적용한 XGBoost모델은 R2 0.6이상, MAE 0.95이하의 평가지표를 보였다. 품종별로는 주황색계열 모델이 가장 좋은 성능을 보였는데, 이는 주황색계열 농가수가 적어 수집된 데이터의 일관성이 높았기 때문으로 풀이된다. 분석에 사용된 입력자료 중 상당기간 누락된 자료는 분석에서 제외함으로써, 전체 조사항목 중 많은 자료가 분석에 활용되지 못한 부분이 본 연구의 한계로 사료된다. 한편 본 연구에서 최적모델로 15주동안의 자료와 17개의 조사항목을 활용했던 점에서 현장에 직접적으로 적용하기에는 제한적이다. 향후 연구에서 차원축소, 주요인자를 활용한 간소화 모델을 개발함으로써 생산량 예측 모델의 적용성을 향상시킬 필요가 있다. 
