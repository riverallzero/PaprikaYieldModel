import pandas as pd
import os

# set files path
p_1 = '../Output/Data/Test/Orange_0'
p_2 = '../Output/Data/Test/Orange_1'
# p_3 = '../Output/Data/Test/Yellow_2'
# p_4 = '../Output/Data/Test/Yellow_3'
# p_5 = '../Output/Data/Test/Yellow_4'
# p_6 = '../Output/Data/Test/Yellow_5'
# merge files
dataFrame = pd.concat(
   map(pd.read_csv, [p_1, p_2]), ignore_index=True)

output_dir = "../Output/Data/Test"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_filename = os.path.join(output_dir, "Orange.csv")
dataFrame.to_csv(output_filename, index=False, encoding="utf-8-sig")

# set files path
o_1 = '../Output/Data/Train/Orange_0'
o_2 = '../Output/Data/Train/Orange_1'
# o_3 = '../Output/Data/Train/Yellow_2'
# o_4 = '../Output/Data/Train/Yellow_3'
# o_5 = '../Output/Data/Train/Yellow_4'
# o_6 = '../Output/Data/Train/Yellow_5'
# merge files
dataFrame = pd.concat(
   map(pd.read_csv, [o_1, o_2]), ignore_index=True)

output_dir = "../Output/Data/Train"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_filename = os.path.join(output_dir, "Orange.csv")
dataFrame.to_csv(output_filename, index=False, encoding="utf-8-sig")