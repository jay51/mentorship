
# 2^8 2^7 2^6 2^5
# 128 64 32 16 8 4 2 1
#  0  0  0  0 1 0 1 0

def binary_to_int(bnum):

    idx = len(bnum) -1  # 8
    base = 0

    result = 0
    while idx >= 0:
        result += int(bnum[idx]) * (2**base)

        base += 1
        idx -= 1

    return result



def int_to_binary(bnum):
    byte = [128, 64, 32, 16, 8, 4, 2, 1]
    binary = ""

    for bit in byte:
        if bit <= bnum:
            binary += "1"
            bnum -= bit
        
        else:
            binary += "0"

    return binary


# def int_to_binary(bnum):
#     byte = [128, 64, 32, 16, 8, 4, 2, 1]
#     binary = ""
#     idx = 0

#     while bnum > 0:

#         if bnum <= byte[idx]:
#             binary += "1"
#             print(binary)
#             bnum -= byte[idx]
#         else:
#             binary += "0"

#         idx += 1

#     return binary



# print(int("0b00001010", 2))

# print(binary_to_int('00001010')) # 10


# print(int_to_binary(10)) # '00001010'


def p1():
    name = input("Name: ")
    age = input("Age: ")
    int_age = int(age)

    deff = 100 - int_age

    year = 2023 + deff
    print(f'you will turn 100 years old in {year}')



# p1()


def p2():
    number = int(input("Number: "))
    
    if number % 2 == 0:
        print("Your number is an even number")
    else:
        print("Your number is an odd number")

# p2()

def p3(a):
    result = []
    for x in a:
        if x < 5:
            result.append(x)

    return result

# print(p3(a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))



def p4(num):

    result = []
    for x in range(1, num+1):
        if num % x == 0:
            result.append(x)

    return result


# print(p4(10))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def p5(a, b):
    result = []
    for x in a:
        for y in b:
            if x == y:
                result.append(x)
    
    return result

def p5(a, b):
    result = []
    for x in a:
        if x in b:
            result.append(x)
    
    return result

# print(p5(a, b))

# def p6(word):
#     len_word = len(word) // 2
#     first_half = word[0 : len_word]
#     second_half = word[len_word:]
#     s_half = ''

#     for char in second_half:
#         s_half = char + s_half

#     if s_half == first_half:
#         print("yes")
#     else:
#         print("no")

    
def p6(word):
    length = len(word)
    for x in range(length//2):
        if word[x] != word[length - x -1]:
            print("NO equal")
            return


    print("YES equal")


    

# pe ep
# pe pe

# print(p6('peep'))


def p7(numbers):
    
    result = [n for n in numbers if n % 2 == 0]

    # result = []
    # for n in numbers:
    #     if n % 2 == 0:
    #         result.append(n)
    
    return result


# print(p7(a))


def p8():
    import random
    # Scissors

    options = ["rock", "paper", "scissor"]
    pc_choice = options[random.randint(0, 2)]
    game_on = True
    while game_on:
        player_choice = input("rock, paper, sccisor: ")
        if player_choice == pc_choice:
            print("Tie")
        if player_choice == "rock" and pc_choice == "scissor":
            print("Player WIN")
        if player_choice == "rock" and pc_choice == "paper":
            print("PC WIN")
        if player_choice == "paper" and pc_choice == "scissor":
            print("PC WIN")           
        if player_choice == "paper" and pc_choice == "rock":
            print("You WIN")
        if player_choice == "scissor" and pc_choice == "paper":
            print("You WIN")
        if player_choice == "scissor" and pc_choice == "rock":
            print("Pc WIN")
        if player_choice not in options:
            print("Invalid option")
        
        play_again = input("YES/NO: ")
        if play_again == "no":
            game_on = False
    

# p8()



def p9():
    
    import random
    random_number = random.randint(1, 9)
    guesses_left = 5
    while guesses_left > 0:
        user_choice = int(input("What number do you choose?"))

        if user_choice > random_number:
            print("Too high")
        if user_choice < random_number:
            print("Too low")
        if user_choice == random_number:
            print("You win")
            break
        guesses_left -= 1

# p9()





a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def is_in(lst, el):
    for elment in lst:
        if elment == el:
            return True
        
    return False




def p10(ls1, ls2):

    result = []

    for num in ls1:
        if is_in(ls2, num) and is_in(result, num) == False:
            result.append(num)
    
    return result


# print(p10(a, b))



def p11(n=0):

    list = [2, 3, 4, 5, 6, 7, 8, 9]
    for individual in list:
        if n != individual and n % individual == 0:
            print(f"{n} is not prime")
            return 
    
    print(f'{n} is prime')




# p11() # 7 is prime




def p12(numbers):
    first = numbers[0]
    last = numbers[len(numbers) - 1]

    return [first, last]

a = [5, 10, 15, 20, 25]
# print(p12(a))



# 0,1 => 1 => 2 => 3
def p13(n):
    current = 1
    prev = 0
    
    for i in range(2, n + 1):
        tmp = current
        current += prev
        prev = tmp
        # print(f'{current:}, {prev:}')
    
    return current



# def p13_2(a):
#     if a <= 2:
#         return 1
    
#     return p13_2(a -1) + p13_2(a -2)





# print(p13_2(30))
a = [5, 5, 5, 10, 10, 15, 20, 25]

def p14(x):
    result = []
    for i in x:
        if x.count(i) == 1:
            result.append(i)

    return result

def p14(x):
    result = set(a)

    return result
# print(p14(a))


def alternate_letters(word):
    result = ""
    flag = False
    for letter in word:
        if flag == False:
            result = result + letter.lower()
            flag = True
            
        elif flag == True:
            result = result + letter.upper()
            flag = False

    return result

# print(alternate_letters("Hello world"))




def p15(statement):
    new = statement.split(" ")
    length_of_list = len(new) # 2 # 0 , 1, 2 
    result = ""
    for x in range(len(new)):
        result += new[length_of_list-1] + " "
        length_of_list -= 1
    
    return result


def p15(statement):
    words = statement.split(" ")
    result = ""
    for word in words:

        result = word + " " + result 
        print(result)
    
    return result

def p15(statement):
    words = statement.split(" ")
    length = len(words) - 1

    result = ""
    for x in range(len(words)):

        if x == length:
            result += words[ length - x ]
        else:
            result += words[ length - x ] + "-"
    
    return result


# print(p15("My name is Michele")) #   Michele is name My




def p16(l=8):
    import random
    possible_char = "0123456789abcdefghijklmnopqrstuvxyz!@#$%^&*"
    password = ""
    for x in range(l):
        random_char = random.choice(possible_char)
        n = random.randrange(1,2)

        if n == 1:
            random_char = random_char.upper()
        else:
            random_char = random_char.lower()


        password += random_char
    
    return password






#print(p16()) # 12345678

#print(p16(10)) # 12345678
#print(p16(16)) # kdfjk@75


def format_word(word, revelied_letters):

    result = ''
    for char in word:
        if char in revelied_letters:
            result += char + " "
        else:
            result += "_ "
        
    return result

# print_word("hello", ["l", 'o'])

# hello

# [l,o]
# _ _ l l 0



def p17(guesses):
    import random

    list = ["running", "jumping", "swiming"]
    random_word = random.choice(list)

    revelied = []
    while guesses:
        
        print(format_word(random_word, revelied), end='')

        letter = input("Guess a letter:")

        if letter in random_word:
            revelied.append(letter)
        else:
            print("Try again")
        


        guesses -= 1

# print(p17(7))


# hello

# _ _ _ _ _ 

# : l 

# _ _ l l _

# : o
# _ _ l l o




def p18(x, y):
    box = '{ }'

    for j in range(y):
        print()
        for i in range(x):
            print(box, end="")

    print()

    #  --- --- --- 
    # |   |   |   | 
    #  --- --- ---  

    # print(box * y)

# p18(6, 6)

def p19():
    import random
    
    heigher = 10
    lower = 1
    computer_choice = 1
    while True:
        # computer_choice = random.randrange(lower, heigher)
        print(f'is your number {computer_choice}')
        # + means the number picked by the computer is heigher than the number in my head
        # - means the number picked by the computer is lower than the number in my head

        answer = input("YES/+/-: ")



        if answer == 'yes':
            break
        if answer == '+':
            heigher = computer_choice 

        if answer == '-':
            lower = computer_choice

        computer_choice +=1 
# 9

# 1 2 3 4 5 6 7 8 9 10

# p19()


def number_length(num):
    result = 0
    while num > 0:
        num = num // 10
        result += 1

    
    return result



# print(number_length(127))



def list_of_multiples(num, length):
    lst = []
    for x in range(1 ,length + 1):
        number = num * x
        lst.append(number)

    return lst



# print(list_of_multiples(7, 5)) # ➞ [7, 14, 21, 28, 35]

# print(list_of_multiples(12, 10))# ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]



def to_dict(chars):

    result = {}
    for char in chars:
        # result[char] = ord(char)
        result.setdefault(char, ord(char))
        
    return result




# {
#     'a': 97,
#     'b': 98,
#     'c': 99
# }

# chars = to_dict(["a", "b", "c"])

# print(chars['b'])
# print(chars.get('b'))

def getLength(nums):
    result = 0
    stack = []
    target = nums
    length = len(nums) -1
    i = 0
    while True:
        if i > length:
            # print(f'max  i:{i} length: {length}')
            if len(stack) == 0:
                break

            # print(f'restore i: {i} el:{target[i]}')
            node = stack.pop()
            target = node[0]
            length = node[1]
            i = node[2]
            # print(f'restore i: {i} el:{target[i]}')
            

        elif type(target[i]) == int:
            result += 1
            # print(f'inside int condition i: {i} el:{target[i]}')

        elif type(target[i]) == list:
            # print(f'inside list condition {target[i]}')
            node = [target, length, i+1]
            stack.append(node)

            target = target[i]
            length = len(target) - 1
            i = -1

        i += 1
        
    return result




# result = 0
def count_elements(nums):
    
    result = 0
    # global result
    for elment in nums:
        if type(elment) == list:
            result += count_elements(elment)

        else:
            result += 1
    

    return result



        

# print(count_elements([1,2,3]))
# print(count_elements([1,2,[1,2], 3]))
# x = [1,2,3, [1,2], [1,2]]
# print(count_elements(x))
# [1,2,3]
# [1,2,[1,2], 3]






# print(getLength([1, [2, 3]]))# 3
# print(getLength([1, [2, [3, 4]]])) # 4
# getLength([1, [2, [3, [4, [5, 6]]]]]) # 6
# getLength([1, [2], 1, [2], 1]) # 5



def reverse_words(word):
    word = list(word)

    for x in range(len(word)//2):
        idx_of_last = len(word) - 1 - x
        tmp = word[idx_of_last]

        word[idx_of_last] = word[x]
        word[x] = tmp


    return word
# def reverse_words(word):
#     reverse = ""
#     for x in word:
#         reverse = x + reverse
    
#     return reverse



# O(n) where n is the length of th word

# O(1)
# O(logN)
# O(n)2

# eulb

# print(reverse_words("blue")) # eulb



def get_indices(elments, item):
    result = []
    for x in range(len(elments)):
        if elments[x] == item:
            result.append(x)

    return result


# time complexity O(N) where n is the length of the list
# space ..        O(N) where n is the length of the list

# print(get_indices(["a", "a", "a", "a", "a", "a", 'a'], "a"))

encoding = {
    "h": '!',
    'e': '@',
    'l': '#',
    'o': '$',
    'w': '%',
    'r': '^',
    "d": '&'
}


# 'hello world' 'irfrrmrrr'
# 'hel'

# ord
# chr

def enc(data):
    import random
    i = 1
    word = ''
    for x in data:
        pos = ord(x) + 1
        word = word + chr(pos)

    #    A * 2 AA 
        for _ in range(i):
            word += chr(random.randrange(33, 127))
            # word += 'A'

        i += 1


    return word
    
# print(enc('hello world')) # !@##$%$^#&




def dec(data):
    i = 0
    inc = 2
    word = ''

    for x in range(len(data)):
        letter = chr(ord(data[i]) - 1)
        word = word + letter

        i += inc
        inc += 1

        if i > len(data):
            break
    

    return word






# data = "i:fq$m\"%=m3l./!D2OYQpa'0-?NxgU*YDp+p@pYu..$Us~mVlJ}cx|mFqsRbfzU**eA4D\7vlMt.h"
# print(chr(ord(data[0]) -1 ))
# print(chr(ord(data[2]) -1 ))
# print(chr(ord(data[5]) -1 ))


# print(dec("i:fq$m\"%=m3l./!D2OYQpa'0-?NxgU*YDp+p@pYu..$Us~mVlJ}cx|mFqsRbfzU**eA4D\7vlMt.h"))




# def enc(data):
#     word = ''
#     for x in data:
#         if encoding.get(x) != None:
#             word = word + encoding.get(x)


#     return word



# def dec(data):#!@##$%$^#&
#     for key in encoding:
#         if encoding[key] in data:
#             data = data.replace(encoding[key], key)

#     return data


# print(enc('helloworld')) # !@##$%$^#&
# print(dec('!@##$%$^#&')) # helloworld


def pprint(arr, v_size, h_size):
    for x in range(v_size):
        x = h_size * x
        # print(f"{arr[x]},  {arr[x+1]}, {arr[x+2]}, {arr[x+3]}")
        for y in range(h_size):
            print(f"{arr[x + y]}, ", end='')
        print()
        
# 3 * 3
# grid = [
#     0,0,0,
#     0,0,0,
#     0,0,0
# ]

# 4 * 4
# grid = [
#     0,0,0,0,
#     0,0,0,0,
#     0,0,0,0,
#     0,0,0,0
# ]


# def set_pos(grid, size, row, col, val):
#     idx = (row -1) * size + col -1

#     grid[idx] = val


# print('--------------------------------')
# pprint(grid, 4)
# print('--------------------------------')

# set_pos(grid, 4, 3, 1, 7)

# print('--------------------------------')
# pprint(grid, 4)
# print('--------------------------------')





# 3 * 4 = rows * cols
# grid = [
#     0,0,0,0,
#     0,0,0,0,
#     0,0,0,0,
# ]



def set_pos(grid, h_size, row, col, val):
    idx = (row -1) * h_size + col -1

    grid[idx] = val





# print('--------------------------------')
# pprint(grid, 3, 4)
# print('--------------------------------')

# set_pos(grid=grid, h_size=4, row=2, col=2, val=7)
# set_pos(grid=grid, h_size=4, row=2, col=1, val=7)
# set_pos(grid=grid, h_size=4, row=1, col=3, val=7)
# set_pos(grid=grid, h_size=4, row=3, col=4, val=7)

# print('--------------------------------')
# pprint(grid, 3, 4)
# print('--------------------------------')






grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]


def print_grid(grid):
    for row in grid:
        print(row)





def set_pos(grid, row, col, val):
    grid[row-1][col-1] = val



# print_grid(grid)

# print('--------------------------------')
# set_pos(grid=grid, row=2, col=2, val=7)

# print_grid(grid)





def reverse_count(x):
    result = []
    max = x
    for number in range(x):
        result.append(max)
        max -= 1


    return result



# print(reverse_count(10)) # [10, 9, 8, 7,6,...]


grid = [
    [0,7,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

# grid = [
#     [0,0,0,0],
#     [0,0,7,0],
#     [0,0,0,0]
# ]




def move_char(grid, row, col, row2, col2):
    # copy = grid[row-1][col-1]

    # grid[row2-1][col2-1] = copy

    # grid[row-1][col-1] = 0



    result = grid[row-1][col-1]
    grid[row-1][col-1] = 0
    grid[row2-1][col2-1] = result
    return grid


# print_grid(move_char(grid, 1, 2, 2, 3))



grid = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
]
# grid = [
#     [0,7,0,7],
#     [0,0,7,0],
#     [0,7,0,7]
# ]

# grid[row-1][col-1] 

# grid[row][col]
# grid[row][col - 2]



def draw_x(grid, row, col):
    
    n_rows = len(grid) - 1
    n_cols = len(grid[0]) - 1

    if row-1 == 0 or row >= n_rows:
        return grid

    if col-1 == 0 or col >= n_cols:
        return grid


    grid[row-1][col-1] = 7 # middle
    grid[row][col-2] = 7 # down and left
    grid[row][col] = 7 # down and right
    grid[row-2][col] = 7 # up and right
    grid[row-2][col-2] = 7 # up and left
    return grid

# result = draw_x(grid, 2, 4)
# print_grid(result)
grid = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
]



def draw_hz_line(grid, x, y, x2, y2, val):
    # x -= 1
    # y -= 1

    row = grid[x-1]
    for i in range(y-1, y2):
        row[i] = val

    return grid

# result = draw_hz_line(grid, 5, 3, 5, 7, 1)
# print_grid(result)


def draw_vz_line(grid, x, y, x2, y2, val):
    
    for i in range(x-1, x2):
        grid[i][y-1] = val

    return grid


# result = draw_vz_line(grid, 2, 5, 5, 5, 1)
# print_grid(result)



def draw_line(grid, x, y, x2, y2, val):
    
    if y != y2:
        col = x
        for i in range(y -1 , y2):
            grid[i][col] = val
            if x != x2:
                col += 1
    else:
        for i in range(x -1 , x2):
            grid[y][i] = val



    return grid


# second col in row 3 to 4th col in row 5
# result = draw_line(grid, 1, 2,        4, 5, 1)
# result = draw_line(grid, 1, 2,        1, 5, 1)
# result = draw_line(grid, 1, 2,        4, 2, 1)
# print_grid(result)






json = {
    'men': [
        {
            'name': 'jack',
            'password': '12345'
        },
        {
            'name': 'nick',
            'password': '46999'
        },
        {
            'name': 'mike',
            'password': '11111'
        },
        {
            'name': 'mark',
            'password': '00000'
        },

    ],
    'women': [
        {
            'name': 'lucy',
            'password': '12345'
        },
        {
            'name': 'sara',
            'password': '46999'
        },
        {
            'name': 'judy',
            'password': '11111'
        },
        {
            'name': 'adaya',
            'password': '00000'
        }
    ]
}


def get_person(json, key, idx):
    result = json[key][idx -1]


    return result



# print(get_person(json, 'women', 1))

def group_teams(json, team1, team2):
    result_boys = json[team1]
    result_girls = json[team2]
    length = len(result_girls)
    
    result = []
    for x in range(length):
        result.append( [result_boys[x], result_girls[x]] )
        # tmp = []
        # tmp.append(result_boys[x])
        # tmp.append(result_girls[x])
        # result.append(tmp)
        

    return result




# print(group_teams(json, 'men', 'women')) # 


result = [ 
    [
        { 'name': 'jack', 'password': '12345' },
        { 'name': 'lucy', 'password': '12345' }
    ],

    [
        { 'name': 'jack', 'password': '12345' },
        { 'name': 'lucy', 'password': '12345' }
    ],

    [
        { 'name': 'jack', 'password': '12345' },
        { 'name': 'lucy', 'password': '12345' }
    ],
]
        


def add_to_team(json, team, person):
    # list = json[team]
    # list.append(person)



    json[team].append(person)
    return json 





import pprint

result = add_to_team(
    json,
    'men',
    {
        'name': 'sam',
        'password': '00000'
    }
)

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(result)


class Person():

    def __init__(self, name, age, h, w):
        self.name = name
        self.age = age
        self.height = h
        self.wieght = w
        self.haircolor = 'brown'


    def print_info(self):
        print(f"{self.name}")
        print(f"{self.age}")
        print(f"{self.height}")
        print(f"{self.wieght}")
        print(f"{self.haircolor}")



# p1 = Person('jack', 28, 5.10, 160)

# p2 = Person('nick', 27, 5.11, 170)

# p2.print_info()

# print('------------')

# p1.print_info()



class Stack():
    def __init__(self, list = []):
        self.list = list


    def add(self, item):
        self.list.append(item)
        return item

    def peak(self):
        return self.list[len(self.list) - 1]

    def pop(self):
        return self.list.pop()
        # del self.list[len(self.list) - 1]



# stack = Stack([1,2,3])

# stack.add(7)
# stack.add(5)
# stack.add(9)

# print(stack.peak()) # 9

# print(stack.pop()) # 9

# print(stack.peak()) # 5



# sign up
#     username: jack
#     password: kjfkadfhhdksajkdfkj


# login
#   username: jack
#   password: kjfkadfhhdksajkdfkj

32
64

# print(hash('passwor')) # kjfkadfhhdksajkdfkj

# password => 32
# hello => 32 


def hash(data):

    word = ''
    for x in range(len(data)):
        # print(data[x])
        if x % 2 == 0:
            pos = ord(data[x]) + 1
            word = word + chr(pos)
        else:
            pos = ord(data[x]) - 1
            word = word + chr(pos)


    i = 122
    v = 1
    if len(word) < 32:
        n = 32 - len(word)
        for x in range(n):
            word += chr(i)
            # print(i, v, x)
            i -= 1
            v += v
            if i - v < 32:
                v = 1
 

    return word

# print(hash('hi'))
# print(hash('hio'))
# print(hash('hioooooooooo'))

# hash password. create all letters exept found in password
def hash(word):
    original_result = []
    #97-122
    for x in word:
        original_result.append(ord(x))
    
    final_result = ""
    for i in range(65, 122):
        if i not in original_result:
            final_result += str(chr(i))

    return final_result

# print(hash('password'))


def hash(data):
    length = len(data)
    first_char = ord(data[0])
    mid_char = ord(data[length // 2])
    last_char = ord(data[length -1])

    sum = (length + first_char + mid_char + last_char) // 2 # 100

    result = ''
    for x in range(32):
        result += chr(40 + sum)
        sum -= 2

    return result

# print(hash('password'))


# Dogs-dating:
    # Dogs
        # - name
        # - age 
        # - type

{
    'keys': 'values'
}