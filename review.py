input = "hello"
input2 = "world"

# camle_case(input) => "hElLo"
# camle_case(input2) => "wOrLd"


def camle_case(word):
    result = ''
    for idx in range(len(word)):
        if idx % 2 == 0:
            result = result + word[idx]   
        else:
            result = result + word[idx].upper()
            
    return result


# result = camle_case('hello')
# print(result)





def camle_case(word):
    result = ''
    flag = False
    for char in word:
        if flag == False:
            result = result + char
            flag = True

        elif flag == True:
            result = result + char.upper()
            flag = False

    return result


# result = camle_case('hello')
# print(result)








# write a function that takes a string and a list of chars and removes those chars from the stirng


def remove_chars(word, chars):
    result = ''
    for char in word:
        if char not in chars:
            result = result + char

    return result


# output = remove_chars('hello world', ['o', 'l'])
# print(output)

def find_idx(word, char):
    lst = []
    for idx in range(len(word)):
        if word[idx] == char:

            lst = lst + idx

    return lst



# word = "Hello world"
# result = find_idx(word, "l")
# result = find_idx(word, "l")
# print(word[2])
# print(word[3])
# print(word[9])
# print(result)




def removing_letters_at_idx(word, idxs):
    var = ""
    for x in range(len(word)):
        if x not in idxs:
            var = var + word[x]
            
    return var


# define = removing_letters_at_idx('running', [2, 0])
# print(define)





# word = "Hello world"
# idxs = [2,3,9]

# removing_letters_at_idx(word, idxs) # => "Heo word"



# write a function that takes 2 args 1st = list of names and 2ed list of names
# return the index for the names in the second list





def find_string(names, find_names): # [0, 3]
    idxs = []
    for idx in range(len(names)):
        if names[idx] in find_names:
            idxs.append(idx)

    return idxs
    

# names = ['jack', 'nick', 'john', 'jamal']
# find_names = ['jack', 'jamal']

# result = find_string(names, find_names)
# print(result)


names = ['jack', 'nick', 'john', 'jamal']
names_to_remove = ['jack', 'jamal']

# remove_names(names, names_to_remove) # ['nick', 'john']
def remove_names(names, find_names):
    result = []
    for name in names:
        if name not in names_to_remove:
            result.append(name)

    return result

# var = remove_names(['jack', 'nick', 'john', 'jamal'], ['jack', 'jamal'])
# print(var)



def is_in(target, input):
    for name in input:
        if name == target:
            return True

    return False


# result1 = is_in('mike', ['jack', 'nick', 'john', 'jamal']) # False
# result2 = is_in('jack', ['jack', 'nick', 'john', 'jamal']) # True

names = ['jack', 'nick', 'john', 'jamal']
names_to_remove = ['jack', 'jamal']

def remove_names(names, find_names):
    result = []
    for name in names:
        if is_in(name, names_to_remove) == False:
            result.append(name)

    return result

# var = remove_names(['jack', 'nick', 'john', 'jamal'], ['jack', 'jamal'])
# print(var)


names1 = ['jack', 'nick', 'john', 'jamal']
names2 = ['jack', 'jamal', 'mike']

def add_to_names(names1, names2): # ['jack', 'nick', 'john', 'jamal', 'mike']
    result = []

    all_names = names1 + names2

    for name in all_names:
        if is_in(name, result) == False:
            result.append(name)

    return result


# save = add_to_names(['jack', 'nick', 'john', 'jamal'], ['jack', 'jamal', 'mike'])
# print(save)


# one sec im reconnecting

def count(word, letter):
    result= 0
    for char in word:
        if char == letter:
            result += 1

    return result

# var = count("dog", "d")
# var2 = count('hello world', 'l') # 3
# print(var)
# print(var2)





def sub(word, idx, letter):
    result = ""
    for x in range(len(word)):
        if x == idx:
            result = result + letter
        else:
            result = result + word[x]

    return result


# print(sub('hello world', 1, 't'))  # htllo world

remove_chars('hello world This a test', [1, 3, 5]) # hloworld This a test


def remove_chars(phrase, index):
    result = ""
    for x in range(len(phrase)):
        if x not in index:
            result = result + phrase[x]
        
    return result

# var = remove_chars("Hello world", [3, 5])
# var2 = remove_chars('hello world This a test', [1, 3, 5]) # hloworld This a test
# print(var)
# print(var2)


def split(word, char):
    result = []
    phrase = "" # 
    for letter in word:
        if letter != char:
            phrase = phrase + letter
        else:
            result.append(phrase)
            phrase = ""

    return result
    

# print(split('jack jamal nick john', ' ')) # ['hello', 'world', 'This', 'is', 'a', 'test']

def replace(words, index, peticular):
    words[index] = peticular

    # result = []
    # for x in range(len(words)):
    #     if x != index:
    #         result.append(words[x])
    #     else: 
    #         result.append(peticular)

    return words
        


# var =replace(['jack', 'john', 'jamal', 'nick'], 1, 'adam') # ['jack', 'adam', 'jamal', 'nick']
# print(var)



to_replace = {
    1: 'adam',
    3: 'jurgen',
    4: 'me',
}

def replace_all(lst, obj):
    for key in obj:
        lst[key] = obj[key]
    
    return lst

def replace_all(lst, obj):
    for i in range(len(lst)):
        if obj.get(i) != None:
            lst[i] = obj[i]
    
    return lst





# print(replace_all(['jack', 'john', 'jamal', 'nick', 'nick'], to_replace)) # ['jack', 'adam', 'jamal', 'nick']



person = {
    'name': 'jack',
    'age': 20,
    'gender': 'male'
}


more_att = {
    'hair_color': 'brown',
    'height': 6.2,
    'weight': 160
}



def add_to_person(person, more_att):
    for key in more_att:
        person[key] = more_att.get(key)

        # person['hair_color'] = 'brown'
        # person['height'] = 6.2

    return person

add_to_person(person, more_att)
person = {
    'name': 'jack',
    'age': 20,
    'gender': 'male',
    'hair_color': 'brown',
    'height': 6.2,
    'weight': 160
}



person1 = {
    'name': 'jack',
    'age': 20,
    'gender': 'male'
}

person2 = {
    'name': 'jack',
    'age': 20,
    'gender': 'female'
}


def equal(person1, person2): # True or False
    for key in person1:
        if person1[key] != person2[key]:
            return False
    
    return True


# var = equal(person1, person2)
# print(var)



person = {
    'name': 'jack',
    'age': 20,
    'gender': 'female',
    'kids': ['jamal', 'jurgen', 'adaya']
}

def add_child(person, lst, key):
    for child in lst:
        children = person[key]
        children.append(child)

    return person
# add_child(person, ['nick', 'james'], 'kids')


person = {
    'name': 'jack',
    'age': 20,
    'gender': 'female',
    'hair_color': 'brown',
    'height': 6.2,
    'weight': 160,
    'kids': ['jamal', 'jurgen', 'adaya'],
}

update_person1 = {
    'gender': 'male',
    'hair_color': 'black',
    'height': 6.7,
}

def update_person(person, update_person1):
    for x in update_person1:
        person[x]= update_person1[x]

    return person

# var1 = update_person(person, update_person1)
# print(var1)



import utils as u
# from utils import add, mul, sub, div
# from utils import *


resut = u.add(1,2)
# resut = add(1,2)
resut = u.sub(1,2)
resut = u.div(1,2)


# print(resut)



def test_update_person():
    person = {
        'name': 'jack',
        'age': 20,
        'gender': 'female',
        'hair_color': 'brown',
        'height': 6.2,
        'weight': 160,
        'kids': ['jamal', 'jurgen', 'adaya'],
    }

    update_person1 = {
        'type': 'male',
        'hair_color': 'black',
        'height': 6.7,
    }
    from utils import update_person

    resutl1 = update_person(person, update_person1)
    # print(resutl1)

    person = {
        'name': 'jack',
        'age': 20,
        'gender': 'female',
        'hair_color': 'brown',
        'height': 6.2,
        'weight': 160,
        'kids': ['jamal', 'jurgen', 'adaya'],
    }

    update_person1 = {
        'type': 'male',
        'hair_color': 'black',
        'height': 6.7,
    }
    resutl1 = update_person(person, update_person1)
    # print(resutl1)






# reverse3([1, 2,          3, 4]) → [4, 3, 2, 1]


# reverse3([5, 11, 9]) → [9, 11, 5]
# reverse3([7, 0, 0]) → [0, 0, 7]

def reverse3(nums):
    length = len(nums) # 3
    result = []
    for i in range(length//2):
        last_el = nums[length - i - 1]
        result.append(last_el)

    return result

def reverse3(nums):
    length = len(nums) # 3
    for i in range(length//2):

        a = nums[i]
        b = nums[length - i - 1]

        nums[i] = b
        nums[length - i - 1] = a

    return nums



# print(reverse3([1, 2, 3, 4]))

# middle_way([1,2 4,6,5 2, 3])

# middle_way([1,2,3,4,5,6])
  

def string_times(word, num):
    new_str = ""
    for _ in range(num):
        new_str = new_str + word
        
    return new_str

def string_times(word, num):
    new_str = word * num
    return new_str


# print(string_times('hello', 2)) # 'HiHi'
# print(string_times('hello', 3)) # 'HiHiHi'
# print(string_times('hello', 1)) # 'Hi'

# def swap():
#     names = [1, 'jack', 56]

#     for i in range(len(names)):
#         if i == 0:
#             t = names[len(names) - 1]
#             names[len(names) - 1] = names[i]
#             names[i] = t

#     return names    


def numbers(array): 
    for x in range(len(array[:4])):
        if array[x] == 9:
            return True

    return False

def numbers(array): 
    copy = array[0: 4]
    for x in copy:
        if x == 9:
            return True

    return False


def numbers(array): 

    # [0,1,2,3]
    for x in range(4):
        if array[x] == 9:
            return True

    return False



def numbers(array): 

    if len(array) < 4:
        return False
    

    result = 9 in array[0: 4]
    return result

# result = numbers([1, 2, 0, 3, 4])
# print(result)




def make_out_word(word1, word2):
    length = len(word1)


    result = word1[:length//2] + word2 + word1[length//2 : length]

    return result





# print(make_out_word('<<>>', 'Yay')) # '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') # '<<WooHoo>>'

# 4 - 2 : 4
def extra_end(word):
    length = len(word) 
    result = word[length -2: length] * 3

    return result





print(extra_end('Hello')) # 'lololo'
extra_end('ab') # 'ababab'
extra_end('Hi') # 'HiHiHi'