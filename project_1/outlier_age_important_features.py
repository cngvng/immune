import pandas as pd
from utils import generate_anomalies

show_outlier = True
data_path = "../data/data_updated.csv"

data = pd.read_csv(data_path)
data = data[data["Health condition"] == "Healthy"]
data = data[data["Age"] < 31]

#data = data[data["Age"] > 30]
#data = data[data["Age"] < 46]

#data = data[data["Age"] > 45]

data_original = data.copy()
data = data.drop(
    columns=['No.', 'Full Name', 'Sample ID', 'Birth year', 'Gioi tinh', 'label', 'Health condition', 'Age', 'Gender'])

data = data[['Q1_ CD21 low', 'Q1_ memory', 'Nkp44 PE-A Median', 'CD8, CD45RA+CD197+',
       'CD4, CD45RA-CD197+', 'CD8, CD45RA+ CD62L+', 'CD8, CD45RA+ CD62L-',
       'CD8, CD45RA-CD197+']]

# generate patiences anomaly for each feature
features_lst = list(data.columns)
anomalies_lst = []

for feature in features_lst:
    x = data[feature]
    patiences_anomaly = generate_anomalies(x)
    anomalies_lst.append(patiences_anomaly)

# get features anomaly for each patience
patience_indices = list(data.index)
dict_patience_anomaly = {}
no_anomalies_patience = []

for i in patience_indices:
    features_anomaly = []
    for j in range(len(anomalies_lst)):
        if i in set(anomalies_lst[j]):
            features_anomaly.append(features_lst[j])
    dict_patience_anomaly[i] = features_anomaly
    no_anomalies_patience.append(len(features_anomaly))

features_anomaly_patience_lst = [dict_patience_anomaly[i] for i in patience_indices]
# no_anomalies_patience = [dict_patience_anomaly[i][1] for i in patience_indices]           

df = pd.DataFrame()
df['Patience index'] = patience_indices
df['Full Name'] = data_original['Full Name'].values
df['Number of anomalies'] = no_anomalies_patience
df['Features anomaly'] = features_anomaly_patience_lst

df.to_excel('./results/task_2/healthy_age/patiences_healthy_age_17-30_important_features_anomaly.xlsx')
#df.to_excel('./results/task_2/healthy_age/patiences_healthy_age_31-45_important_features_anomaly.xlsx')
#df.to_excel('./results/task_2/healthy_age/patiences_healthy_age_over_45_important_features_anomaly.xlsx')


