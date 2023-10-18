import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def correlation_matrix(data=None, label=None, threshold=None):
    # select all columns of numeric types (including the label column if applicable)
    num_col = list(data.select_dtypes(include='number').columns)

    if label:
        # compute pairwise correlation of columns
        corr_matrix = data[num_col].corr()

        # corr. value between X and Y, where X = 'label' and Y is an arbitrary column
        corr_xy_given_x_is_label = abs(corr_matrix['label'])

        most_corr_values = corr_xy_given_x_is_label[abs(corr_xy_given_x_is_label) > threshold]
        most_corr_values = most_corr_values.sort_values(ascending=False)
        most_corr_values = most_corr_values.drop(labels=['label'])

        multi_cols = most_corr_values.index

    else:
        num_col.remove('label')

        corr_matrix = (data[num_col].corr())

        corr_features_mean = corr_matrix.mean(axis=0)

        most_corr_values = corr_features_mean[(corr_features_mean) > threshold]

        multi_cols = most_corr_values.index

        multi_cols = pd.Index(list(multi_cols) + ['label'])
    return multi_cols, most_corr_values


def plot_boxplot_and_swarmplot(data, columns, identifier_vars, value_name, plot_title, show_outlier, fig_name,
                               rotation=0):
    data_melt = pd.melt(data[columns], id_vars=identifier_vars, var_name="", value_name=value_name)

    plt.figure(figsize=(16, 9))
    sns.set(style="whitegrid")
    plt.title(plot_title)

    ax = sns.boxplot(x="", y=value_name, hue=identifier_vars, data=data_melt, palette="Set1", showfliers=show_outlier)
    ax = sns.swarmplot(x="", y=value_name, hue=identifier_vars, data=data_melt, palette="Set1")
    plt.xticks(rotation=rotation)
    # ax.xaxis.label.set_fontsize(20)

    # plt.show()
    plt.savefig(fig_name)


def generate_anomalies(x):
    values_high = x[x > np.median(x)]
    values_low = x[x < np.median(x)]

    Q3 = max(values_high[values_high <= np.median(values_high)])
    Q1 = min(values_low[values_low >= np.median(values_low)])

    IQR = Q3 - Q1

    max_normal = max(values_high[values_high <= Q3 + 1.5 * IQR])
    min_normal = min(values_low[values_low >= Q1 - 1.5 * IQR])

    anomalies_high = x[x > max_normal]
    anomalies_low = x[x < min_normal]
    anomalies = anomalies_high.append(anomalies_low)
    patiences_anomaly = list(anomalies.index)

    return patiences_anomaly

# data1_percent_melt = pd.melt(data1[cols_percent_data1], id_vars="Health condition", var_name="",
#                value_name="cells %")

# data1_cells_melt = pd.melt(data1[cols_cells_data1], id_vars="Health condition", var_name="",
#                value_name="cells per \u03bcl blood")

# plt.figure(figsize=(16,9))
# sns.set(style="whitegrid")

# plt.title("Total cell count")

# ax = sns.boxplot(x="", y="cells %", hue='Health condition',data = data1_percent_melt, showfliers = True)
# ax = sns.swarmplot(x="", y="cells %", hue='Health condition', data=data1_percent_melt, color="red")

# plt.show()
# plt.savefig("./figs/task_1/data1_percent.png")
