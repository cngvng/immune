# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 20:10:27 2022

@author: cngvng
"""

import pandas as pd
from utils import compare_distributions_by_p_value_with_threshold

show_outlier = True
identifier_vars = 'Health condition'
data_path = "../data/data_updated.csv"

data = pd.read_csv(data_path)

"""HEALTH CONDITION"""
data_healthy = data[data["Health condition"] == "Healthy"]
data_sepsis = data[data["Health condition"] == "Sepsis"]

data_healthy = data_healthy.drop(columns=['No.', 'Full Name', 'Sample ID', 'Birth year', 'Gioi tinh', 'label', 'Health condition', 'Age', 'Gender'])
data_sepsis = data_sepsis.drop(columns=['No.', 'Full Name', 'Sample ID', 'Birth year', 'Gioi tinh', 'label', 'Health condition', 'Age', 'Gender'])

threshold = 0.0001

df = compare_distributions_by_p_value_with_threshold(data_1=data_healthy, 
                                                data_2=data_sepsis, 
                                                threshold = threshold)

df.to_excel('./results/task_1/health_condition/important_p-value_healthy_sepsis.xlsx')