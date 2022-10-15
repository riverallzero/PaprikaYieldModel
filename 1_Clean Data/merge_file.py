import pandas as pd
import os

# set files path
p_or = '../Output/Data/paprika(Orange).csv'
p_re = '../Output/Data/paprika(Red).csv'
p_ye = '../Output/Data/paprika(Yellow).csv'

# merge files
dataFrame = pd.concat(
   map(pd.read_csv, [p_or, p_re, p_ye]), ignore_index=True)

output_dir = "../Output/Data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_filename = os.path.join(output_dir, "paprika_all.csv")
dataFrame.to_csv(output_filename, index=False, encoding="utf-8-sig")