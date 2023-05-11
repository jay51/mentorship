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

# name = 'adaya'
# age = 23
# query = f"INSERT INTO customer(name, age) VALUES('{name}', {age})"
# print(query)

# cur.execute(query)
# conn.commit()


# Execute a query
# cur.execute("SELECT * FROM postgres")
cur.execute("SELECT datname FROM pg_database")

# Retrieve query results
records = cur.fetchall()
for row in records:
    print(row)