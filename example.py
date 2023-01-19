import random

name = input("What is your name? \n")
print(f"Welcome to the GUESS game {name}\n")
print("Let's start playing\n")
print(f"{name} you have to guess a random number that computer is choosing from 0 to 100 in 7 tries\n")

random_number = random.randint(0, 101)
print(random_number)

tries = 3

while True:
    guess = int(input("What is your guess?\n"))
    if guess == random_number:
        print(f"Good jooob {name}, you got it, you found the random number {random_number}\nYou deserve a kiss!! ")
        print("****************** YOU WIN *****************")
        break
    

    tries -= 1
    if tries == 0:
        print(f"{name} you are a loooser, you didn't find number {random_number}")
        print("")
            
        print("*****************  GAME OVER  ****************")
        break

    if guess < random_number:
        print(f"*** Your guess is lower than random number.\n Try again...")
        print(f"You have {tries} more tries left")
    
    elif guess > random_number:
        print(f"**** Your guess is greater than random number.\n Try again...")
        print(f"You have {tries} more tries left")




    


