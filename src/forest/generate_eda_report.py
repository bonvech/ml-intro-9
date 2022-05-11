#!python3

import pandas as pd
import pandas_profiling

print("Pandas version", pd.__version__)


df = pd.read_csv('../../data/train.csv')
print(df.shape)
print(df.head())

pandas_profiling.ProfileReport(df).to_file("forest_eda_report.html")
