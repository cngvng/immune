import pandas as pd
from utils import plot_boxplot_and_swarmplot, correlation_matrix

threshold = 0.35
label = True  # Fasle for correlation without label
show_outlier = True

data_path = "../data/data_updated.csv"
data = pd.read_csv(data_path)

"""HEALTH CONDITION"""
data = data[data["Health condition"] == "Healthy"]
data = data[data["Age"] < 40]

# make label be gender
label_gender = []
for i in list(data.index):
    if data['Gender'][i] == 'Male':
        label_gender.append(1)
    else:
        label_gender.append(0)
data['label'] = label_gender

data_original = data.copy()

data = data.drop(
    columns=['No.', 'Full Name', 'Sample ID', 'Birth year', 'Gioi tinh', 'Health condition', 'Age', 'Gender'])

features_selected, features_ranking  = list(correlation_matrix(data, label=label, threshold=threshold))

# save important features
df = pd.DataFrame()
df['Important features'] = list(features_ranking.index)
df['Correlation level'] = list(features_ranking.values)
  
df.to_excel("./results/task_3/gender_young/important_features_healthy_gender_young.xlsx")

#only healthy
features_selected_percent = [feature for feature in features_selected if feature[0:3]!='Abs'] + ['Gender']
features_selected_cells = [feature for feature in features_selected if feature[0:3]=='Abs'] + ['Gender']

fig_name = "./results/task_3/gender_young/key_features_percent_young.png"
plot_title = "Important features in cell % or % positive (age < 40)"
value_name = "cell % or % positive"
identifier_vars = 'Gender'
rotation = 10


plot_boxplot_and_swarmplot(data_original, features_selected_percent, identifier_vars, value_name, plot_title,
                            show_outlier, fig_name, rotation)

if len(features_selected_cells) > 1:
    # only for healthy
    fig_name = "./results/task_3/gender_young/key_features_cell_young.png"
    plot_title = "Important features in cell count (age < 40)"
    value_name = "cells per \u03bcl blood"
    rotation = 0
    
    plot_boxplot_and_swarmplot(data_original, features_selected_cells, identifier_vars, value_name, plot_title,
                                show_outlier, fig_name, rotation)
