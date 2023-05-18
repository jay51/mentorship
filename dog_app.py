
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

username = input("username: ")
password = input("password: ")

login_query = f"select * from owners where name='{username}' and password='{password}'"
cur.execute(login_query)

user = cur.fetchone()
print(user)
run = True

if user is None:
    print(f"invalid username or password")
    run = False


while run:
    print(
        """
        1) Search for Dog by name
        2) Insert a new dog
        3) Search for my Dogs

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
        query = f"""
        INSERT INTO dogs(name, breed, gender, age, characteristic, status, owner_id)
        VALUES('{name}', '{breed}', '{gender}', {age}, '{characteristic}', '{status}', {user[0]})
        """
        print(query)
        cur.execute(query)
        conn.commit()
    

    if answer == "3":
        owner_id = user[0]
        query = f"SELECT * FROM dogs WHERE owner_id = {owner_id}"
        cur.execute(query)
        records = cur.fetchall()
        for dog in records:
            print(dog)

    
    if answer == '-1':
        break





