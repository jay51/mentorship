
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
