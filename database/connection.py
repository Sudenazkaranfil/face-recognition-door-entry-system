import psycopg2

def get_connection():
    # Define the necessary parameters to establish a connection to the PostgreSQL database.
    # Replace the empty strings with your actual database credentials.
    return psycopg2.connect(
        dbname="",          # Name of your PostgreSQL database (e.g., "face_db")
        user="postgres",    # Username for your database (commonly "postgres")
        password="",        # Password for your database user
        host="localhost",   # Host address (usually "localhost" for local testing)
        port="5432"         # Port number (default for PostgreSQL is 5432)
    )
