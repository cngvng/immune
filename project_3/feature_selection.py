import pandas as pd
from utils import plot_boxplot_and_swarmplot, correlation_matrix

threshold = 0.7
label = True  # Fasle for correlation without label
show_outlier = True

data_path = "../data/data_updated.csv"
data = pd.read_csv(data_path)

"""HEALTH CONDITION"""
data_healthy = data[data["Health condition"] == "Healthy"]
data_sepsis = data[data["Health condition"] == "Sepsis"]

data = data_healthy.append(data_sepsis)
data_original = data.copy()

data = data.drop(
    columns=['No.', 'Full Name', 'Sample ID', 'Birth year', 'Gioi tinh', 'Health condition', 'Age', 'Gender'])

features_selected = list(correlation_matrix(data, label=label, threshold=threshold))

features_selected_cells = ['Abs CD3', 'Abs CD8', 'Abs Lympho', 'Abs CD4'] + ['Health condition']
features_selected_percent = ['Lympho.2', 'Mono', 'Lympho.4', 'Lympho.3', 'Lympho.6'] + ['Health condition']

fig_name = "./figs/task_3/key_features_cells.png"
plot_title = "Important features in cell count"
value_name = "cells per \u03bcl blood"
identifier_vars = 'Health condition'
rotation = 0

plot_boxplot_and_swarmplot(data_original, features_selected_cells, identifier_vars, value_name, plot_title,
                           show_outlier, fig_name, rotation)

fig_name = "./figs/task_3/key_features_percent.png"
plot_title = "Important features in cell % or % positive"
value_name = "cell % or % positive"

plot_boxplot_and_swarmplot(data_original, features_selected_percent, identifier_vars, value_name, plot_title,
                           show_outlier, fig_name, rotation)
