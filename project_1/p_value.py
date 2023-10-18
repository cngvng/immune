from scipy import stats
import pandas as pd
from utils import plot_boxplot_and_swarmplot

show_outlier = True
identifier_vars = 'Health condition'
data_path = "../data/data_updated.csv"

data = pd.read_csv(data_path)

"""GENDER p-value"""
data = data[data["Health condition"] == "Healthy"]
data_male = data[data["Gender"] == "Male"]
data_female = data[data["Gender"] == "Female"]

data_male = data_male.drop(columns=['No.', 'Full Name', 'Sample ID', 'Birth year', 'Gioi tinh', 'label', 'Health condition', 'Age', 'Gender'])
data_female = data_female.drop(columns=['No.', 'Full Name', 'Sample ID', 'Birth year', 'Gioi tinh', 'label', 'Health condition', 'Age', 'Gender'])

features_lst = list(data_male.columns)
p_values_lst = []

for feature in features_lst:
    x = data_male[feature].values
    y = data_female[feature].values
    p_value = stats.ttest_ind(x, y)[1]
    p_values_lst.append(p_value)

df = pd.DataFrame()
df['Features'] = features_lst
df['p-value'] = p_values_lst
   
df.to_excel('./results/task_1/healthy_gender/p-value_healthy_gender.xlsx')

"""AGE GROUP p-value"""
data = pd.read_csv(data_path)
data = data[data["Health condition"] == "Healthy"]

# define and add age group columns to data
age_group_lst = []
for i in range(len(data)):
    age = data['Age'][i]
    if age > 45:
        age_group_lst.append('> 45')
    elif age > 30 and age <= 45:
        age_group_lst.append('31-45')
    else:
        age_group_lst.append('17-30')

data['Age group'] = age_group_lst
data.insert(0, 'Age group', data.pop('Age group'))

data = data.drop(columns=['No.', 'Full Name', 'Sample ID', 'Birth year', 'Gioi tinh', 'label', 'Health condition', 'Gender', 'Age'])

data_young = data[data["Age group"] == "17-30"]
data_middle = data[data["Age group"] == "31-45"]
data_old = data[data["Age group"] == "> 45"]

data_young = data_young.drop(columns=['Age group'])
data_middle = data_middle.drop(columns=['Age group'])
data_old = data_old.drop(columns=['Age group'])

features_lst = list(data_young.columns)
p_values_young_middle_lst = []
p_values_young_old_lst = []
p_values_middle_old_lst = []

for feature in features_lst:
    x = data_young[feature].values
    y = data_middle[feature].values
    z = data_old[feature].values
    
    p_value_young_middle = stats.ttest_ind(x, y)[1]
    p_value_young_old = stats.ttest_ind(x, z)[1]
    p_value_middle_old = stats.ttest_ind(y, z)[1]
    
    p_values_young_middle_lst.append(p_value_young_middle)
    p_values_young_old_lst.append(p_value_young_old)
    p_values_middle_old_lst.append(p_value_middle_old)
    

df = pd.DataFrame()
df['Features'] = features_lst
df['p-value young-middle'] = p_values_young_middle_lst
df['p-value young-old'] = p_values_young_old_lst
df['p-value middle-old'] = p_values_middle_old_lst
   
df.to_excel('./results/task_1/healthy_age/p-value_healthy_age.xlsx')