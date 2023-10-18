import pandas as pd
from utils import plot_boxplot_and_swarmplot

show_outlier = True
data_path = "../data/data_updated.csv"

data = pd.read_csv(data_path)
data = data[data["Health condition"] == "Sepsis"]

data = data.drop(columns=['No.', 'Full Name', 'Sample ID', 'Birth year', 'Gioi tinh', 'label'])

data1 = data[list(data.columns[3:16]) + ['Gender']]  # cells % and cells per ul blood
data2 = data[list(data.columns[16:26]) + ['Gender']]  # % positive
data3 = data[list(data.columns[26:38]) + ['Gender']]  # cells %
data4 = data[list(data.columns[38:65]) + ['Gender']]  # cells %
data5 = data[list(data.columns[65:80]) + ['Gender']]  # cells %
data6 = data[list(data.columns[80:92]) + ['Gender']]  # MFI NK, cells %
data7 = data[list(data.columns[92:98]) + ['Gender']]  # NK YTOTOXICITY (%), T cell PROLIFERATION

"=========Process Dataset 1 - Total cell count============"
cols_percent_data1 = ['% CD3', '% CD4', '% CD8', '%CD19', '% CD56', '4/8 ratio', 'Gender', 'Abs mono']
cols_cells_data1 = list(data1.columns.drop(cols_percent_data1)) + ['Gender']

columns = cols_percent_data1
fig_name = "./figs/task_1/sepsis_gender/data1_sepsis_gender_percent.png"
plot_title = "Dataset 1 - Total cell count"
value_name = "cell %"
identifier_vars = 'Gender'
rotation = 0

plot_boxplot_and_swarmplot(data1, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, rotation)

columns = cols_cells_data1
fig_name = "./figs/task_1/sepsis_gender/data1_sepsis_gender_cells.png"
plot_title = "Dataset 1 - Total cell count"
value_name = "cells per \u03bcl blood"
identifier_vars = 'Gender'

plot_boxplot_and_swarmplot(data1, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, rotation)

"=========Process Dataset 2 - LYMPHOCYTE AND MONOCYTE SUBPOPULATIONS============"
columns = list(data2.columns)
fig_name = "./figs/task_1/sepsis_gender/data2_sepsis_gender_percent.png"
plot_title = "Dataset 2 - Lymphocyte and monocyte subpopulations"
value_name = "% positive"
identifier_vars = 'Gender'
rotation = 10

plot_boxplot_and_swarmplot(data2, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, rotation)

"=========Process Dataset 3 - B CELLS SUBPOPULATIONS============"
columns = list(data3.columns)
fig_name = "./figs/task_1/sepsis_gender/data2_sepsis_gender_percent.png"
plot_title = "Dataset 3 - B cells subpopulations"
value_name = "cell %"
identifier_vars = 'Gender'
rotation = 10

plot_boxplot_and_swarmplot(data3, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, rotation)

# plot features having small values
columns = ['CD21low_CD38low', 'Transitional', 'plasmablasts', 'Q1_ immature', 'Gender']
fig_name = "./figs/task_1/sepsis_gender/data3_sepsis_gender_percent_small.png"
plot_boxplot_and_swarmplot(data3, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, 0)

"=========Process Dataset 4 - T CELLS SUBPOPULATIONS============"
columns = list(data4.columns)
fig_name = "./figs/task_1/sepsis_gender/data4_sepsis_gender_percent.png"
plot_title = "Dataset 4 - T cells subpopulations"
value_name = "cell %"
identifier_vars = 'Gender'
rotation = 45

plot_boxplot_and_swarmplot(data4, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, rotation)

columns_first = columns[0:13] + ['Gender']
columns_second = columns[13:]

rotation = 10
fig_name = "./figs/task_1/sepsis_gender/data4_sepsis_gender_percent_first.png"
plot_boxplot_and_swarmplot(data4, columns_first, identifier_vars, value_name, plot_title, show_outlier, fig_name,
                           rotation)

rotation = 30
fig_name = "./figs/task_1/sepsis_gender/data4_sepsis_gender_percent_second.png"
plot_boxplot_and_swarmplot(data4, columns_second, identifier_vars, value_name, plot_title, show_outlier, fig_name,
                           rotation)

"=========Process Dataset 5 - NK AND T ACTIVATION AND MATURATION============"
columns = list(data5.columns)
fig_name = "./figs/task_1/sepsis_gender/data5_sepsis_gender_percent.png"
plot_title = "Dataset 5 - NK and T activation and maturation"
value_name = "cell %"
identifier_vars = 'Gender'
rotation = 10

plot_boxplot_and_swarmplot(data5, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, rotation)

"=========Process Dataset 6 - NK CELL RECEPTOR============"
columns = list(data6.columns)
plot_title = "Dataset 6 - NK cell receptor"
value_name = "cell %"
identifier_vars = 'Gender'
rotation = 0

columns_percent = columns[0:6] + ['Gender']
fig_name = "./figs/task_1/sepsis_gender/data6_sepsis_gender_percent.png"
plot_boxplot_and_swarmplot(data6, columns_percent, identifier_vars, value_name, plot_title, show_outlier, fig_name,
                           rotation)

columns_mfi = columns[6:]
fig_name = "./figs/task_1/sepsis_gender/data6_sepsis_gender_mfi.png"
plot_boxplot_and_swarmplot(data6, columns_mfi, identifier_vars, value_name, plot_title, show_outlier, fig_name,
                           rotation)

columns_mfi_p44 = columns[7:8] + ['Gender']
fig_name = "./figs/task_1/sepsis_gender/data6_sepsis_gender_mfi_p44.png"
plot_boxplot_and_swarmplot(data6, columns_mfi_p44, identifier_vars, value_name, plot_title, show_outlier, fig_name,
                           rotation)

"=========Process Dataset 7 - NK CYTOTOXICITY AND T CELL PROLIFERATION============"
columns = list(data7.columns)
plot_title = "Dataset 7 - NK cytotoxicity and T cell proliferation"
value_name = "NK cytotoxicity %"
identifier_vars = 'Gender'
rotation = 0

fig_name = "./figs/task_1/sepsis_gender/data7_sepsis_gender_percent.png"
plot_boxplot_and_swarmplot(data7, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name, rotation)
