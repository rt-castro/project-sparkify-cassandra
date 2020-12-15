import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv
from cassandra.cluster import Cluster
from conf import *
from nosql_queries import *


def create_consolidated_csv(newfile, column_headers, filedir):
    """
    Description: 
        - Gets all the CSV files under the specified directory and
        consolidated them into a single CSV file
        - Removes unwanted rows from the CSV files

    Arguments:
        - newfile: Name of the consolidated CSV file
        - column_headers: List of headers to be used as the column names for the consolidated CSV file
        - filedir: Subfolder location of the data files to be processed and consolidated

    Returns:
        - None
    """
    
    file_path_list = []

    # Get your current folder and subfolder event data
    filepath = os.getcwd() + filedir

    # Creates a list of filepath where the files are located 
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.csv'))
        for f in files:
            if '.ipynb_checkpoints' in f:
                pass
            else:
                file_path_list.append(os.path.abspath(f))
            
    full_data_rows_list = [] 
    
    for f in file_path_list:
        # Reads the CSV file 
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            # Creates a csv reader object 
            csvreader = csv.reader(csvfile) 
            # Skip header
            next(csvreader)
        
            # Extracts each data row one by one and append its        
            for line in csvreader:
                full_data_rows_list.append(line) 


    # Creates a consolidated csv file that will be used to insert data into the Apache Cassandra tables
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with open(newfile, 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(column_headers)
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            else:
                writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))


def process_data(session, newfile):
    """
    Description: 
        - Reads the consolidated CSV file and extracts the data for ingestion
        - Inserts the data onto the appropriate table based on the insert query from the `insert_queries_list`
        - Queries onto each table to extract the needed data based on the select quries from `select_queries_list`
        - Prints the results for validation and analysis

    Arguments:
        - session: Used in executing the queries
        - newfile: Name of the consolidated CSV file

    Returns:
        - None
    """
    
    # Reads the consolidated CSV file
    with open(newfile, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        
        # Skip header
        next(csvreader)
        
        # Executes the insert statements for each query
        for line in csvreader:
            query_insert = insert_queries_list[0].strip() # Query 1 (song_details_library)
            query_insert1 = insert_queries_list[1].strip() # Query 2 (session_details_library)
            query_insert2 = insert_queries_list[2].strip() # Query 3 (user_history_library)
            try:
                session.set_keyspace(keyspace)
                session.execute(query_insert, (int(line[8]), int(line[3]), line[0], line[9], float(line[5])))
                session.execute(query_insert1, (int(line[10]), int(line[8]), int(line[3]), line[0], line[9], line[1], line[4]))
                session.execute(query_insert2, (line[9], int(line[10]), line[1], line[4]))
            except Exception as e:
                print(e)
    
    # Executes the select statements for each query
    query_select = select_queries_list[0].strip() # Query 1 (song_details_library)
    query_select1 = select_queries_list[1].strip() # Query 2 (session_details_library)
    query_select2 = select_queries_list[2].strip() # Query 3 (user_history_library)
    try:
        rows = session.execute(query_select) # Query 1 (song_details_library)
        rows1 = session.execute(query_select1) # Query 2 (session_details_library)
        rows2 = session.execute(query_select2) # Query 3 (user_history_library)
    except Exception as e:
        print(e)
        
    # Prints the results of the select statements
    for row in rows:
        print('Query 1 results: ', row.artist, ',', row.song, ',', row.length)

    for row in rows1:
        print('Query 2 results: ', row.artist, ',', row.song, ',', row.first_name + ' ' + row.last_name)
        
    for row in rows2:
        print('Query 3 results: ', row.first_name + ' ' + row.last_name)
        
        
def main():
    """
    Description: 
        - Establishes the connection to the Cassandra server
        - Calls the function that will create the consolidated CSV file
        - Calls the function that will initialize the ETL workflow
        - Closes the connection to the server

    Arguments:
        - None

    Returns:
        - None
    """
    
    # Runs an initial script that initializes the tables
    os.system(initial_script)
    
    # Establishes a session to connect to the Cassandra server
    try:
        cluster = Cluster(hosts)
        session = cluster.connect()
    except Exception as e:
        print(e)
        
    create_consolidated_csv(newfile, column_headers, filedir='/event_data')
    process_data(session, newfile)
    
    session.shutdown()
    cluster.shutdown()

    
if __name__ == "__main__":
    main()