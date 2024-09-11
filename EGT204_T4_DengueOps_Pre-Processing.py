import os
import pandas as pd

#1. ADDING COLUMN HEADERS & COMBINING INTO 1 DF - COMBINED_DATASET.CSV
#----------------------------------------------------------------------

#a. Path Initialisation
CWD = os.getcwd()
CSV_DIR = os.path.join(CWD, 'csv')

#b. Column names
column_headers = ['num_cases', 'street_address', 'latitude', 'longitude', 'cluster_num', 'recent_cases_in_cluster', 'total_cases_in_cluster', 'date', 'month_num']

#c. Reading the files in the csv folder into dfs
csv_contents = os.listdir(CSV_DIR)

if '.DS_Store' in csv_contents:
    csv_contents.remove('.DS_Store')


#d. For each CSV file add column headers and merge everything into 1 big df
for file in csv_contents:
    if (file[-4:] != '.csv') or (file == 'combined_dataset.csv'):
        continue
    
    #adding column headers into the df
    file_path = os.path.join(CSV_DIR, file)
    df = pd.read_csv(file_path, header=None)
    df.columns = column_headers

    #merging all 257 dfs into 1 df
    if len(temp_df) > 0:
        temp_df = pd.concat([temp_df, df])
    else:
        temp_df = df


#e. Storing the merged df as a CSV file
temp_df.to_csv(os.path.join(CSV_DIR, 'combined_dataset.csv'))