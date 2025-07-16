
# This script connects to a PostgreSQL database using psycopg2
# and retrieves the database version
import psycopg2

# Define connection parameters
conn = psycopg2.connect(
    host="localhost",         # e.g. "localhost" or IP address
    port="5432",              # default PostgreSQL port
    database="postgres",  # Replace with your database name
    user="postgres",  # Replace with your PostgreSQL username
    password="pa55w0rd"  # Replace with your PostgreSQL password
)

# Create a cursor to perform database operations
cursor = conn.cursor()

# Example: Fetch version
cursor.execute("SELECT version();")
print("Database version:", cursor.fetchone())

# Close the cursor and connection
cursor.close()
conn.close()
