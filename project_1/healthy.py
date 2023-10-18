import pandas as pd
from utils import plot_boxplot_and_swarmplot

show_outlier = True
data_path = "../data/data_updated.csv"

data = pd.read_csv(data_path)

"""HEALTH CONDITION"""
data = data[data["Health condition"] == "Healthy"]
data_original = data.copy()

data = data.drop(columns=['No.', 'Full Name', 'Sample ID', 'Birth year', 'Gioi tinh', 'label'])

data1 = data[list(data.columns[3:16]) + ['Health condition']]  # cells % and cells per ul blood
data2 = data[list(data.columns[16:26]) + ['Health condition']]  # % positive
data3 = data[list(data.columns[26:38]) + ['Health condition']]  # cells %
data4 = data[list(data.columns[38:65]) + ['Health condition']]  # cells %
data5 = data[list(data.columns[65:80]) + ['Health condition']]  # cells %
data6 = data[list(data.columns[80:92]) + ['Health condition']]  # MFI NK, cells %
data7 = data[list(data.columns[92:98]) + ['Health condition']]  # NK YTOTOXICITY (%), T cell PROLIFERATION

"=========Process Dataset 1 - Total cell count============"
cols_percent_data1 = ['% CD3', '% CD4', '% CD8', '%CD19', '% CD56', '4/8 ratio', 'Health condition', 'Abs mono']
cols_cells_data1 = list(data1.columns.drop(cols_percent_data1)) + ['Health condition']

columns = cols_percent_data1
fig_name = "./results/task_1/healthy/data1_percent.png"
plot_title = "Dataset 1 - Total cell count"
value_name = "cell %"
identifier_vars = 'Health condition'
rotation = 0

plot_boxplot_and_swarmplot(data1, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, rotation)

columns = cols_cells_data1
fig_name = "./results/task_1/healthy/data1_cells_count.png"
plot_title = "Dataset 1 - Total cell count"
value_name = "cells per \u03bcl blood"
show_outlier = True

plot_boxplot_and_swarmplot(data1, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, rotation)

"=========Process Dataset 2 - LYMPHOCYTE AND MONOCYTE SUBPOPULATIONS============"
columns = list(data2.columns)
fig_name = "./results/task_1/healthy/data2_percent.png"
plot_title = "Dataset 2 - Lymphocyte and monocyte subpopulations"
value_name = "% positive"
rotation = 10

plot_boxplot_and_swarmplot(data2, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, rotation)

"=========Process Dataset 3 - B CELLS SUBPOPULATIONS============"
columns = list(data3.columns)
fig_name = "./results/task_1/healthy/data3_percent.png"
plot_title = "Dataset 3 - B cells subpopulations"
value_name = "cell %"
rotation = 10

plot_boxplot_and_swarmplot(data3, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, rotation)

# plot features having small values
columns = ['CD21low_CD38low', 'Transitional', 'plasmablasts', 'Q1_ immature', 'Health condition']
fig_name = "./results/task_1/healthy/data3_percent_small.png"
plot_boxplot_and_swarmplot(data3, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, 0)

"=========Process Dataset 4 - T CELLS SUBPOPULATIONS============"
columns = list(data4.columns)
fig_name = "./results/task_1/healthy/data4_percent_all.png"
plot_title = "Dataset 4 - T cells subpopulations"
value_name = "cell %"
rotation = 45

plot_boxplot_and_swarmplot(data4, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, rotation)

columns_first = columns[0:13] + ['Health condition']
columns_second = columns[13:]

rotation = 10
fig_name = "./results/task_1/healthy/data4_percent_first.png"
plot_boxplot_and_swarmplot(data4, columns_first, identifier_vars, value_name, plot_title, show_outlier, fig_name,
                           rotation)

rotation = 30
fig_name = "./results/task_1/healthy/data4_percent_second.png"
plot_boxplot_and_swarmplot(data4, columns_second, identifier_vars, value_name, plot_title, show_outlier, fig_name,
                           rotation)

"=========Process Dataset 5 - NK AND T ACTIVATION AND MATURATION============"
columns = list(data5.columns)
fig_name = "./results/task_1/healthy/data5_percent.png"
plot_title = "Dataset 5 - NK and T activation and maturation"
value_name = "cell %"
rotation = 10

plot_boxplot_and_swarmplot(data5, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, rotation)

"=========Process Dataset 6 - NK CELL RECEPTOR============"
columns = list(data6.columns)
plot_title = "Dataset 6 - NK cell receptor"
value_name = "cell %"
rotation = 0

columns_percent = columns[0:6] + ['Health condition']
fig_name = "./results/task_1/healthy/data6_percent.png"
plot_boxplot_and_swarmplot(data6, columns_percent, identifier_vars, value_name, plot_title, show_outlier, fig_name,
                           rotation)

columns_mfi = columns[6:]
fig_name = "./results/task_1/healthy/data6_mfi.png"
plot_boxplot_and_swarmplot(data6, columns_mfi, identifier_vars, value_name, plot_title, show_outlier, fig_name,
                           rotation)

columns_mfi_p44 = columns[7:8] + ['Health condition']
fig_name = "./results/task_1/healthy/data6_mfi_p44.png"
plot_boxplot_and_swarmplot(data6, columns_mfi_p44, identifier_vars, value_name, plot_title, show_outlier, fig_name,
                           rotation)

"=========Process Dataset 7 - NK CYTOTOXICITY AND T CELL PROLIFERATION============"
columns = list(data7.columns)
plot_title = "Dataset 7 - NK cytotoxicity and T cell proliferation"
value_name = "NK cytotoxicity %"
identifier_vars = 'Health condition'
rotation = 0

fig_name = "./results/task_1/healthy/data7_percent.png"
plot_boxplot_and_swarmplot(data7, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, rotation)
