# SPARKIFY - APACHE CASSANDRA

CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Schema Design
 * Project Files
 * Configuration
 * Process
 * Maintainers
 

INTRODUCTION
------------

 * A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.

 * They'd like to have an Apache Cassandra database which can create queries on song play data to answer some questions. This project aims to create a database using the provided data, and wherein the user can efficiently query on the tables in the database.

 * Users will use the following logic in when querying to the database (Sample queries):
 
     - Query 1: Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4
     
     - Query 2: Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182
     
     - Query 3: Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'


REQUIREMENTS
------------

This project utilizes the following technologies:

 * **Software**
 
    - *Anaconda* (https://www.anaconda.com/products/individual)

      Used to run the .ipynb files, and also to test the validity of the ETL process 
 
   - *Apache Cassandra* (https://cassandra.apache.org/download/)

     The NoSQL Database that this project utilizes.
     
   - *Python* (https://www.python.org/downloads/)

     The main language where the project is based on.
 
 * **Python Libraries** (does not come built-in with the Python or Anaconda software download)
    
   - *cassandra-driver* (https://pypi.org/project/cassandra-driver/)

     A modern, feature-rich and highly-tunable Python client library for Apache Cassandra (2.1+) and DataStax Enterprise (4.7+) using exclusively Cassandra’s binary protocol and Cassandra Query Language v3.
 
 
TABLE DESIGN
-------------

 * **song_details_library** - answers the logic in query 1, giving the artist, song title and song's length in the music app history based on the sessionId and itemInSession
    
    - *columns: artist, song, length, session_id, item_in_session
       
 * **session_details_library** - answers the logic in query 2, giving the artist, song title, and user name in the music app history based on the userId and sessionId and sorted by iteminSession and the first and last name of the user.
    
    - *columns: artist, song, first_name, last_name, user_id, session_id, item_in_session
       
 * **user_history_library** - answers the logic in query 3, giving every user name in my music app history who listened to a particular song
 
    - *columns: song, first_name, last_name, user_id, session_id


PROJECT FILES
-------------

 * Configuration
 
    - **conf.py**: contains the connection details and variables to be used in producing the CSV file.
 
 * Create Tables
 
    - **create_keyspace_tables.py**: It accesses the default cassandra database to create the database *sparkifydb*, and drop the existing query tables if they exist, and then recreate them.
    
 * ETL
 
    - **nosql_queries.py**: Contains the queries that will be processed in the ETL workflow.
    
    - **etl_nosql.py**: Runs the whole ETL process - creating the connection to the cassandra database, reading the CSV files, consolidating them into a single CSV file, and then ingesting them to the database.
    
    - **Project_1B_ Project_Template.ipynb**: A more sequential and detailed breakdown of each of the main processes in the ETL workflow.

 * Test
 
    - **test.ipynb**: Tests whether the files were successfully ingested and queryable.

   
CONFIGURATION
-------------
 
 * Configure the connection credentials in the **conf.py** file to simulate your local production:

    - **column_headers**: List of column headers to be used by the consoliated CSV file.

    - **hosts**: Connection to a Cassandra instance.

    - **keyspace**: Name of the keyspace that you will be using.
    
 * Configure the connection credentials in the **nosql_queries.py** file to simulate your local production:

    - **keyspace_create**: This is the query that will create the keyspace in the cassandra database.

    - **drop_tables_list**: List of queries that will drop the tables.

    - **create_tables_list**: List of queries that will create the tables.
    
    - **insert_queries_list**: List of queries that will insert the data into the tables.
    
    - **select_queries_list**: List of queries that will select the data from the tables to validate the ETL process.
    

PROCESS
-------

 * Configure the **conf.py** to replicate the connection details of your local production.
 * Run the **etl_nosql.py** to extract the data from the JSON files and ingest them to the created database.
 * Run the **test.ipynb** to check whether the data ingestion was successful.


MAINTAINERS
-----------

Current maintainers:
 * Robert Carlo T. Castro (rt-castro) - https://www.github.com/rt-castro