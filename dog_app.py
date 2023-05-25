
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

def login(username, password):
    login_query = f"select * from owners where name='{username}' and password='{password}'"
    print(login_query)
    cur.execute(login_query)

    user = cur.fetchone()
    return user


user = None
run = True

asking = input("Sign up / Log-in 1 or 2:  ")

if asking != '1' and asking != '2':
    print("invalid option")
    exit()

username = input("USERNAME: ")
password = input("PASSWORD: ")

invalid_words = ['update', 'delete', 'insert', 'select']
for word in invalid_words:
    if word in username or word in password:
        print("can't hack me")
        exit()



# 12345'); update dogs set owner_id = 77 --
if asking == "1":
    query = f"INSERT INTO owners (name, password) VALUES ('{username}', '{password}')"
    print(query)
    cur.execute(query)
    conn.commit()
    user = login(username, password)

elif asking == '2':
    user = login(username, password)


if user is None:
    print(f"invalid username or password")
    run = False


while run:
    print(
        """
        1) Search for Dog by name
        2) Insert a new dog
        3) Search for my Dogs
        4) Delete Dog by id

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

    if answer == "4":
        id = input("What is your dogs id?")
        query = f"Delete From dogs WHERE id = {id}"
        cur.execute(query)
        conn.commit()
        print("Your dog has successfully been deleted")

    
    if answer == '-1':
        break





