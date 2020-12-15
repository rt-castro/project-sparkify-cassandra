import cassandra
from cassandra.cluster import Cluster
from conf import *
from nosql_queries import *


def create_keyspace():
    """
    Description: 
        - Establishes the connection to the Cassandra server
        - Sets the cluster and session variable
        - Creates the keyspace for the project

    Arguments:
        - None

    Returns:
        - cluster
        - session
    """
    try:
        # Connect to Cassandra server
        cluster = Cluster(hosts)
        session = cluster.connect()
        
        # Create the keyspace to be used
        session.execute(keyspace_create)
    except Exception as e:
        print(e)
        
    return cluster, session


def drop_tables(session):
    """
    Description: 
        - Drops each table in the `drop_tables_list` list

    Arguments:
        - session: Used in executing the queries

    Returns:
        - None
    """
    
    try:
        session.set_keyspace(keyspace)
        for query in drop_tables_list[:]:
            rows = session.execute(query)
    except Exception as e:
        print(e)

        
def create_tables(session):
    """
    Description: 
        - Creates each table in the `create_tables_list` list

    Arguments:
        - session: Used in executing the queries

    Returns:
        - None
    """
    
    try:
        session.set_keyspace(keyspace)
        for query in create_tables_list[:]:
            rows = session.execute(query)
    except Exception as e:
        print(e)

        
def main():
    """
    Description: 
        - Establishes the connection to the Postgres server
        - Sets the cursor variable
        - Calls the function that will initialize the ETL workflow
        - Closes the connection to the server

    Arguments:
        - None

    Returns:
        - None
    """
    
    cluster, session = create_keyspace()
    
    drop_tables(session)
    create_tables(session)
    
    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()