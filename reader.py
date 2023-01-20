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
    




while True:
  
    print("""
    1- search User
    2- Add User
    3- exit

    """)

    value = input(">: ")

    if value == "1":
        print('search user')

    elif value == "2":
        print('add user')

    elif value == "3":
        break
    else:
        print("invalid optin")






