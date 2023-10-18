from scipy import stats
import pandas as pd

show_outlier = True
identifier_vars = 'Health condition'
data_path = "../data/data_updated.csv"

data = pd.read_csv(data_path)

"""HEALTH CONDITION"""
data_healthy = data[data["Health condition"] == "Healthy"]
data_sepsis = data[data["Health condition"] == "Sepsis"]

data_healthy = data_healthy.drop(columns=['No.', 'Full Name', 'Sample ID', 'Birth year', 'Gioi tinh', 'label', 'Health condition', 'Age', 'Gender'])
data_sepsis = data_sepsis.drop(columns=['No.', 'Full Name', 'Sample ID', 'Birth year', 'Gioi tinh', 'label', 'Health condition', 'Age', 'Gender'])

features_lst = list(data_sepsis.columns)
p_values_lst = []

for feature in features_lst:
    h = data_healthy[feature].values
    s = data_sepsis[feature].values
    p_value = stats.ttest_ind(h, s)[1]
    p_values_lst.append(p_value)

df = pd.DataFrame()
df['Features'] = features_lst
df['p-value'] = p_values_lst
   
df.to_excel('./results/task_1/health_condition/p-value_healthy_sepsis.xlsx')
