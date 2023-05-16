# pip install psycopg2-binary

import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    dbname='dogs-dating',
    user='postgres',
    password='password',
    host='140.238.136.84',
    port=5432
)

# Open a cursor to perform database operations
cur = conn.cursor()

name = 'jurgen'
age = 25
query = f"INSERT INTO customer(name, age) VALUES('{name}', {age})"
print(query)

# cur.execute(query)
# conn.commit()


# Execute a query
cur.execute("SELECT * FROM dogs")
# cur.execute("SELECT datname FROM pg_database")

# Retrieve query results
records = cur.fetchall()
# print(records[0][1], records[1])




for row in records:
    print(row)