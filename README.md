# Evaluation-selection

https://github.com/rolling-scopes-school/ml-intro/blob/2022/9_evaluation_selection/HOMEWORK.md

# EDA profiling report
To obtain EDA profiling report of the data run script 
```
python3 generate_eda_report.py
```
If you have an error 
```
[Pandas-profiling] ImportError: cannot import name 'ABCIndexClass' from 'pandas.core.dtypes.generic'
```
try to do next steps

    1. Edit the file "~/[your_conda_env_path]/lib/site-packages/visions/dtypes/boolean.py"
    2. Find the row "from pandas.core.dtypes.generic import ABCIndexClass, ABCSeries" and just replace ABCIndexClass for ABCIndex.
    3. Save the boolean.py file and enjoy your report!
