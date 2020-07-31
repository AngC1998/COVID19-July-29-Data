import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import csv
from sklearn.linear_model import LinearRegression

states_dictionary = {}
cases_dictionary = {}
state_dictionary = {}
case_dictionary = {}
overall_dictionary = {}
cases_columns = []
states_columns = []
overall_columns = []
overall_array = []

with open('confirmedcases.csv') as csv_file_one:
    csv_reader = csv.reader(csv_file_one, delimiter = ',')
    index = 0
    for row in csv_reader:
        state_name = ''
        entries = []
        if index == 0:
            index_two = 0
            for entry in row:
                cases_dictionary[entry] = []
                cases_columns.append(entry)
                if entry == 'state':
                    state_name = entry
                else:
                    entries.append(entry)
        else:
            for i in range(0, len(cases_columns)):
                col = cases_columns[i]
                arr = cases_dictionary[col]
                if col == 'state':
                    state_name = row[i]
                    arr.append(row[i])
                elif col == 'cases' or col == 'deaths':
                    arr.append(int(row[i]))
                    entries.append(int(row[i]))
                else:
                    arr.append(row[i])
                    entries.append(row[i])
                cases_dictionary[col] = arr
        case_dictionary[state_name] = entries
        index += 1

with open('csvData.csv') as csv_file_two:
    csv_reader = csv.reader(csv_file_two, delimiter = ',')
    index = 0
    for row in csv_reader:
        state_name = ''
        entries = []
        if index == 0:
            index_two = 0
            for entry in row:
                states_dictionary[entry.lower()] = []
                states_columns.append(entry.lower())
                if index_two == 0:
                    state_name = entry.lower()
                else:
                    entries.append(entry.lower())
                index_two += 1
        else:
            for i in range(0, len(states_columns)):
                col = states_columns[i]
                arr = states_dictionary[col]
                if i == 0:
                    state_name = row[i]
                    arr.append(row[i])
                elif i == (len(cases_columns) - 1):
                    arr.append(float(row[i]))
                    entries.append(float(row[i]))
                else:
                    arr.append(int(row[i]))
                    entries.append(int(row[i]))
                states_dictionary[col] = arr
        state_dictionary[state_name] = entries
        index += 1
#print(cases_dictionary)
#print(states_dictionary)
overall_columns = ['state'] + case_dictionary['state'] + state_dictionary['\ufeff\"state\"']
for state in case_dictionary:
    if state != 'state':
        first_array = case_dictionary[state]
        overall_arr = []
        if state not in state_dictionary:
            overall_arr = [state] + first_array + [0, 0, 0, 0, 0]
            overall_array.append(overall_arr)
        else:
            second_array = state_dictionary[state]
            overall_arr = [state] + first_array + second_array
            overall_array.append(overall_arr)
#print(overall_columns)
#print(overall_array)
for entry in overall_columns:
    overall_dictionary[entry] = []
for entry in overall_array:
    for i in range(0, len(entry)):
        if i == 0 or i == 1:
            arr = overall_dictionary[overall_columns[i]]
            arr.append(entry[i])
            overall_dictionary[overall_columns[i]] = arr
        elif i == len(entry) - 2:
            arr = overall_dictionary[overall_columns[i]]
            arr.append(float(entry[i]))
            overall_dictionary[overall_columns[i]] = arr
        else:
            arr = overall_dictionary[overall_columns[i]]
            arr.append(int(entry[i]))
            overall_dictionary[overall_columns[i]] = arr
print(overall_dictionary)
df = pd.DataFrame(data=overall_dictionary)
#print(df)
#print(df.shape)
#print(df.head)
#print(df.columns)
#print(df.nunique(axis=0))
#print(df.describe())
df_cleaned = df.copy()
df_cleaned = df_cleaned.copy().drop(['date', 'fips', 'landarea', 'waterarea'], axis=1)
df_cleaned = df_cleaned[df_cleaned['cases'] > 0]
df_cleaned = df_cleaned[df_cleaned['totalarea'] > 0]
print(df_cleaned)
#print(df_cleaned.shape)
#print(df_cleaned.head)
#print(df_cleaned.columns)
#print(df_cleaned.nunique(axis=0))
#print(df_cleaned.describe())
df_cleaned.plot(kind='scatter', x='pop', y='cases')
pop_arr_orig = overall_dictionary['pop']
cases_arr_orig = overall_dictionary['cases']
pop_arr = np.asarray(overall_dictionary['pop'])
cases_arr = np.asarray(overall_dictionary['cases'])
print(pop_arr)
print(cases_arr)