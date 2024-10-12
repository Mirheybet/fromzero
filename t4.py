import numpy as np
import pandas as pd

csv_data = pd.read_csv("sample_data.csv")
salary= csv_data['Salary']
salary= np.mean(salary)
print(salary)     