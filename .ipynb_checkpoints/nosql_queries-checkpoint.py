# QUERIES

keyspace_create = "CREATE KEYSPACE IF NOT EXISTS sparkifydb WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"

drop_tables_list = [
    # Query 1 (song_details_library)
    "DROP TABLE IF EXISTS song_details_library", 
    # Query 2 (session_details_library)
    "DROP TABLE IF EXISTS session_details_library",
    # Query 3 (user_history_library)
    "DROP TABLE IF EXISTS user_history_library"
]

create_tables_list = [
    # Query 1 (song_details_library)
    """
    CREATE TABLE IF NOT EXISTS song_details_library (artist text, song text, length double, 
    session_id int, item_in_session int, PRIMARY KEY ((session_id, item_in_session)))
    """,
    # Query 2 (session_details_library)
    """
    CREATE TABLE IF NOT EXISTS session_details_library (artist text, song text, first_name text, last_name text, 
    user_id int, session_id int, item_in_session int, PRIMARY KEY ((user_id, session_id), 
    item_in_session, last_name, first_name))
    """, 
    # Query 3 (user_history_library)
    """
    CREATE TABLE IF NOT EXISTS user_history_library (song text, first_name text, last_name text, 
    user_id int, session_id int, PRIMARY KEY ((song), user_id, session_id, last_name, first_name))
    """
]

insert_queries_list = [
    # Query 1 (song_details_library)
    """
    INSERT INTO song_details_library (artist, song, length, session_id, item_in_session) VALUES (%s, %s, %s, %s, %s)
    """,
    # Query 2 (session_details_library)
    """
    INSERT INTO session_details_library (artist, song, first_name, last_name, user_id, session_id, item_in_session) VALUES
    (%s, %s, %s, %s, %s, %s, %s)
    """,
    # Query 3 (user_history_library)
    """
    INSERT INTO user_history_library (song, first_name, last_name, user_id, session_id) VALUES (%s, %s, %s, %s, %s)
    """
]

select_queries_list = [
    # Query 1 (song_details_library)
    """
    SELECT * FROM song_details_library
    WHERE session_id = 338 AND item_in_session = 4
    """,
    # Query 2 (session_details_library)
    """
    SELECT * FROM session_details_library
    WHERE user_id = 10 AND session_id = 182
    """,
    # Query 3 (user_history_library)
    """
    SELECT * FROM user_history_library
    WHERE song = 'All Hands Against His Own'
    """
]