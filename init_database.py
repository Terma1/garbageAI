import sqlite3

def setup_database(db_file, sql_file):
    """
    Opens or creates an SQLite database and executes the SQL script.
    """
    try:
        # Connect to SQLite database (creates the file if it doesn't exist)
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # Read the SQL script from file
        with open(sql_file, 'r') as f:
            sql_script = f.read()

        # Execute the SQL script
        cursor.executescript(sql_script)

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print("Database setup completed successfully.")
    except Exception as e:
        print(f"Error setting up database: {e}")

# Example usage
setup_database("data/garbage_collection.db", "db_migrations/create_database.sql")
setup_database("data/garbage_collection.db", "db_migrations/insert_mappings.sql")
setup_database("data/garbage_collection.db", "db_migrations/add_view.sql")