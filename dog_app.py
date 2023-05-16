
import psycopg2
import config

# Connect to your postgres DB
conn = psycopg2.connect(
    dbname=config.dbname,
    user=config.user,
    password=config.password,
    host=config.host,
    port=config.port
)

# Open a cursor to perform database operations
cur = conn.cursor()




while True:
    print(
        """
        1) Search for Dog by name
        2) Insert a new dog
        3) Search for Dogs by owner

        type -1 to exit
        
        """
    )

    answer = input("> ")

    if answer == "1":
        name = input("Name?: ")
        query = f"select * from dogs where name = '{name}'"
        cur.execute(query)
        record = cur.fetchone()
        print(record)

    if answer == "2":
        name = input("Name?: ")
        breed = input("What breed: ")
        gender = input("What gender: ")
        age = input("age: ")
        characteristic = input("What characteristics: ")
        status= input("status: ")
        query = f"INSERT INTO dogs(name, breed, gender, age, characteristic, status) VALUES('{name}', '{breed}', '{gender}', {age}, '{characteristic}', '{status}')"
        print(query)
        cur.execute(query)
        conn.commit()
    

    if answer == "3":
        owner_id = input("owner id?: ")
        query = f"SELECT * FROM dogs WHERE owner_id = {owner_id}"
        cur.execute(query)
        records = cur.fetchall()
        for dog in records:
            print(dog)

    
    if answer == '-1':
        break





