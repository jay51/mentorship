file = open("./text", "w")

while True:

    print("What would you like to choose?")
    print("1. Add to file")
    print("2. Exit")

    choice = input("1 or 2 \n")
    if choice == "1":
        second_choice = input("What would you like to add to file?:")
        file.write(second_choice + "\n")
        file.flush()

    elif choice == "2":
        file.close()
        break


    else:
        print("Nope")
        break

    

            

