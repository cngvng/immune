import pandas as pd
from utils import plot_boxplot_and_swarmplot, correlation_matrix

threshold = 0.5
label = True  # Fasle for correlation without label
show_outlier = True

data_path = "../data/data_updated.csv"
data = pd.read_csv(data_path)

"""HEALTH CONDITION"""
data = data[data["Health condition"] == "Healthy"]
data = data[data["Age"] > 30]

# define and add age group columns to data
age_group_lst = []
for i in list(data.index):
    age = data['Age'][i]
    if age > 45:
        age_group_lst.append('> 45')
    elif age > 30 and age <= 45:
        age_group_lst.append('31-45')
    else:
        age_group_lst.append('17-30')

data['Age group'] = age_group_lst
data.insert(0, 'Age group', data.pop('Age group'))

# make label be age group
label_age_group = []
for i in list(data.index):
    age = data['Age'][i]
    if age > 45:
        label_age_group.append(2)
    elif age > 30 and age <= 45:
        label_age_group.append(1)
    else:
        label_age_group.append(0)

data['label'] = label_age_group
data_original = data.copy()

data = data.drop(
    columns=['No.', 'Full Name', 'Sample ID', 'Birth year', 'Gioi tinh', 'Health condition', 'Age', 'Gender', 'Age group'])

features_selected, features_ranking  = list(correlation_matrix(data, label=label, threshold=threshold))

# save important features
df = pd.DataFrame()
df['Important features'] = list(features_ranking.index)
df['Correlation level'] = list(features_ranking.values)
  
df.to_excel("./results/task_3/age/important_features_healthy_age_middle_old.xlsx")

#only healthy
features_selected_percent = [feature for feature in features_selected if feature[0:3]!='Abs'] + ['Age group']
features_selected_cells = [feature for feature in features_selected if feature[0:3]=='Abs'] + ['Age group']

fig_name = "./results/task_3/age/key_features_percent_middle_old.png"
plot_title = "Important features in cell % or % positive"
value_name = "cell % or % positive"
identifier_vars = 'Age group'
rotation = 10


plot_boxplot_and_swarmplot(data_original, features_selected_percent, identifier_vars, value_name, plot_title,
                            show_outlier, fig_name, rotation)

if len(features_selected_cells) > 1:
    # only for healthy
    fig_name = "./results/task_3/age/key_features_cell_middle_old.png"
    plot_title = "Important features in cell count"
    value_name = "cells per \u03bcl blood"
    
    plot_boxplot_and_swarmplot(data_original, features_selected_cells, identifier_vars, value_name, plot_title,
                                show_outlier, fig_name, rotation)
