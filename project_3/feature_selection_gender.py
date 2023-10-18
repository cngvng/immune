import pandas as pd
from utils import plot_boxplot_and_swarmplot, correlation_matrix

threshold = 0.26
label = True  # Fasle for correlation without label
show_outlier = True

data_path = "../data/data_updated.csv"
data = pd.read_csv(data_path)

"""HEALTH CONDITION"""
data_healthy = data[data["Health condition"] == "Healthy"]
data_sepsis = data[data["Health condition"] == "Sepsis"]

data = data_healthy.append(data_sepsis)
# data = data_healthy
# data = data_sepsis

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

features_selected = list(correlation_matrix(data, label=label, threshold=threshold))

# both healthy and sepsis or only sepsis
features_selected_percent = features_selected[1:7] + ['Gender']

# only healthy
# features_selected_percent = ['PBMNCs (10^6)', 'NK cell.6', 'NK cells.1', 'B cells.3', 'NK cells.5', '% CD4'] + ['Gender']
# features_selected_cells = ['Abs CD8', 'Abs Lympho', 'Abs CD56', 'Abs CD3'] + ['Gender']

fig_name = "./figs/task_3/gender/both_healthy_sepsis/key_features_percent.png"
# fig_name = "./figs/task_3/gender/sepsis/key_features_percent.png"
plot_title = "Important features in cell % or % positive"
value_name = "cell % or % positive"
identifier_vars = 'Gender'
rotation = 0


plot_boxplot_and_swarmplot(data_original, features_selected_percent, identifier_vars, value_name, plot_title,
                            show_outlier, fig_name, rotation)

# # only for healthy
# fig_name = "./figs/task_3/gender/healthy/key_features_cell.png"
# plot_title = "Important features in cell count"
# value_name = "cells per \u03bcl blood"

# plot_boxplot_and_swarmplot(data_original, features_selected_cells, identifier_vars, value_name, plot_title,
#                            show_outlier, fig_name, rotation)
