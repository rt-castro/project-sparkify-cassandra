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
    CREATE TABLE IF NOT EXISTS session_details_library (user_id int, session_id int, 
    item_in_session int, artist text, song text, first_name text, last_name text,
    PRIMARY KEY ((user_id, session_id), item_in_session))
    """, 
    # Query 3 (user_history_library)
    """
    CREATE TABLE IF NOT EXISTS user_history_library (song text, user_id int, first_name text, last_name text, 
    PRIMARY KEY ((song), user_id))
    """
]

insert_queries_list = [
    # Query 1 (song_details_library)
    """
    INSERT INTO song_details_library (session_id, item_in_session, artist, song, length) VALUES (%s, %s, %s, %s, %s)
    """,
    # Query 2 (session_details_library)
    """
    INSERT INTO session_details_library (user_id, session_id, item_in_session, artist, song, first_name, last_name) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """,
    # Query 3 (user_history_library)
    """
    INSERT INTO user_history_library (song, user_id, first_name, last_name) VALUES (%s, %s, %s, %s)
    """
]

select_queries_list = [
    # Query 1 (song_details_library)
    """
    SELECT artist, song, length FROM song_details_library
    WHERE session_id = 338 AND item_in_session = 4
    """,
    # Query 2 (session_details_library)
    """
    SELECT artist, song, first_name, last_name FROM session_details_library
    WHERE user_id = 10 AND session_id = 182
    """,
    # Query 3 (user_history_library)
    """
    SELECT first_name, last_name FROM user_history_library
    WHERE song = 'All Hands Against His Own'
    """
]