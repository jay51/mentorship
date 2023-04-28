
import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(dbname='test', user='postgres', password='password', host='173.255.194.114')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM users")

# Retrieve query results
records = cur.fetchall()
print(records)