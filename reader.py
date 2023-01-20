# file = open('./math', "r")

# content  = file.readline()
# print(content[0])
# print(content[1])



# for i in range(len(content)):
#     if i != 2:
#         line = content[i]
#         print(line)
#     else:
#         break
# file = open("text", "a")

# file.write(content)
# x = 3
# while x >= 3 and x <= 5:
#     file.write(content[x])
#     file.flush()
#     x += 1

# file.close
    
3
def get_all_users_except(id):
    file = open("./passwords.csv", "r")
    lines = file.readlines()
# [
# 'id,name,password',
# '1,jamal,123456',
# '2,jay,126kdjsadk',

# '4,nick,123456jskdjf',
# '5,jurgen,123456kajsdf',
# ]
    result = []
    for line in lines:

        # ['1', 'jamal' ,'123456']
        values = line.split(',')
        if values[0] != id:
            result.append(line)

    file.close()
    return result


def find_user(name):
    file = open("./passwords.csv", "r")
    lines = file.readlines()
# [
# 'id,name,password',
# '1,jamal,123456',
# '2,jay,126kdjsadk',
# '3,jack,123456jsdkfj',
# '4,nick,123456jskdjf',
# '5,jurgen,123456kajsdf',
# ]
    result = []
    for line in lines:

        # ['1', 'jamal' ,'123456']
        values = line.split(',')
        if values[1] == name:
            result.append(line)

    file.close()
    return result

        # if name in line:
        #     pass


def add_user(id, name, password):
    file = open("./passwords.csv", "a")
    combo = f"{id},{name},{password}\n"
    file.write(combo)
    file.flush()
    file.close()



file = open("./passwords.csv", "r")
id = len(file.readlines())
file.close

while True:
  
    print("""
    1- search User
    2- Add User
    3- Delet User
    4- exit

    """)

    value = input(">: ")

    if value == "1":
        name = input("User Name: ")
        result = find_user(name) # ['1,jamal, 123456', '2,jamal,54321']
        for line in result:
            print(line)


    elif value == "2":
        ask_name = input("What is your name?")
        ask_password = input("What is your password?")
        add_user(id, ask_name, ask_password)
        id +=1 

    elif value == "3":
        user_id = input("user_id: ")
        users = get_all_users_except(user_id)

        file = open('./passwords.csv', 'w')
        for user in users:
            file.write(user)
            file.flush()
        
        file.close()
    
    elif value == "4":
        break
    else:
        print("invalid optin")






