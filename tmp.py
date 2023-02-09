
def find_nth(numbers, nth):
    if len(numbers) < nth:
        return False

    unq_nums = []
    for n in numbers:
        if n not in unq_nums:
            unq_nums.append(n)

    unq_nums = sorted(unq_nums)
    return unq_nums[len(unq_nums) - nth]


# max_number = find_nth([3,3,4,6,7,8,7,8], 3) # 6
# print(max_number, "expect: 6")

# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#  [3, 6, 9]


# person = {'name': 'jamal', 'age': 25}
# person['name'] # 'jamal'


def get_val_from_dict(person, value):
    values = list(person.values())
    keys = list(person.keys())
    idx = values.index(value)
    return keys[idx]
    # print(values)
    # print(keys)




# result = get_val_from_dict(person, 'jamal') # name
# print(result)


url = "https://www.google.com/search?q=cats&tbm=isch"
# "http://www.google.com/search?q=cats"

# url = "http://google.com" # web


# url = "http//www.google.com"
# url =  "https/www.googlecom" # web

# "postgresql://yourdb.db/test" # database
# "postgresql://yourdb.db/test" # database

def is_http_url(url):
    url_prts = url.split(":")
    http = url_prts[0]
     

    if http != 'http' and http != 'https': 
        return False

    uri = url_prts[1]
    slashes = uri[0: 2]

    if slashes != '//':
        return False

    domain = uri[2: ]
    domain = domain.split('.')

    if len(domain[0]) == 0:
        return False
    
    return True




# print(is_http_url(url)) # True or False

def make_http_url(prot, domain, ext):
    if prot != "http" and prot != "https":
        return False
    variable = f"{prot}://{domain}.{ext}"
    return variable


# print(make_http_url('https', 'google', 'edu')) # http://google.edu



def extract_url(url):
    http = url.split(":")[0]
    domain = url.split(":")[1].split(".")




# url = "https://www.google.com/search?q=cats&tbm=isch"
# extract_url(url) # ['https', 'www.google', 'com']


numbers = [3,1,2]

def sort(nums):
    new_lst = []
    for _ in range(len(nums)):
        s = min(nums)
        new_lst.append(s)
        nums.remove(s)
    

    return new_lst


# print(sort(numbers))

def increment():
    print('1')

# class Counter():

#     count = 0

#     def increment():
#         Counter.count += 1
#         return Counter.count

#     def decrement():
#         Counter.count -= 1
#         return Counter.count


class Counter():

    count = 0

    def increment(self):
        self.count += 1
        return self.count

    def decrement(self):
        self.count -= 1
        return self.count

# print(Counter.increment()) # -> 1 
# print(Counter.increment()) # -> 2 
# print(Counter.increment()) # -> 3 
# print(Counter.decrement()) # -> 2 

# my_counter1 = Counter()
# my_counter2 = Counter()

# print(my_counter1.increment()) # -> 1 
# print(my_counter1.increment()) # -> 2 

# print(my_counter2.increment()) # -> 1 


class Player():
    name = ""
    health = 100
    skill = 1

    # def modify_health(self):
    #     self.health += 5

    # def rename(self, new_name):
    #     self.name = new_name


def modify_health(self):
    self.health += 5

def rename(self, new_name):
    self.name = new_name

player1 = Player()
player2 = Player()

# player1.name = "Jurgen"
# player2.name = "Adaya"

# player1.rename("Jurgen")
# player2.rename("Adaya")

rename(player1, "Jurgen")
rename(player2, "Adaya")

player1.skill = 5
player2.skill = 6

# player1.modify_health()
# player2.modify_health()

modify_health(player1)
modify_health(player2)

# print(player1.name, player1.skill, player1.health)
# print(player2.name, player2.skill, player2.health)

class Animal():
    name = ""
    type = ""
    age = 0

    def set_age(self, given_age):
        self.age = given_age

def set_name(self, given_name):
    self.name = given_name

def set_type(self, given_type):
    self.type = given_type


animal1 = Animal()
animal2 = Animal()
set_name(animal1, "z")
set_name(animal2, "l")
set_type(animal1, "zebra")
set_type(animal2, "lion")
animal1.set_age(27)
animal2.set_age(28)

# print(animal1.name, animal1.type, animal1. age)
# print(animal2.name, animal2.type, animal2. age)


class Math():

    total = 0

    def add(self, num):
        self.total += num
    
    def sub(self, num):
        self.total -= num

    def div(self, num):
        self.total /= num

    def mult(self, num):
        self.total *= num


m1 = Math()
m2 = Math()

m1.add(2)
m1.mult(4)

m2.add(3)
m2.mult(6)

class Person():
    plant = 'Earth'

    def __init__(self, name, age, skills):
        self.skills = skills
        self.name = name
        self.age = age

    def set_skill(self, skill):
        self.skills.append(skill)


p1 = Person('jack', 20, [])
p2 = Person('nick', 30, ['driving'])

p1.set_skill("running")
p1.set_skill("playing chess")

p2.set_skill("driving")

# print(p1.name)
# print(p1.age)
# print(p1.skills)

# print(p2.name)
# print(p2.age)
# print(p2.skills)





class Queue():
    
    def __init__(self):
        self._queue = []

    def enqueue(self, item):
        self._queue.append(item)


    def peek(self):
        if len(self._queue) == 0:
            return None

        return self._queue[0]

    def dequeue(self):
        if len(self._queue) == 0:
            return None

        return self._queue.pop(0)


# y = Queue()
# x = Queue()

# y.enqueue(1)
# y.enqueue(2)

# x.enqueue('first element')
# x.enqueue('second element')

# print(y.peek())
# print(x.peek())


# y.dequeue()
# y.dequeue()

# x.dequeue()


# print(y.peek())
# print(x.peek())




class Enemy():

    kills = []

    def __init__(self, health, name):
        self.health = health
        self.name = name


    def print_info(self):
        print(self.health)
        print(self.name)
        print(self.kills)

    def kill(self, name):
        self.kills = []
        self.kill.append(name)


enemy_1 = Enemy(100, "John")

enemy_2 = Enemy(80, "Jack")

# enemy_1.print_info()
# enemy_2.print_info()

# enemy_1.name = "Brown"

# enemy_1.print_info()
# enemy_2.print_info()

# enemy_1.kill("Jamal")
# enemy_2.kill("Jurgen")




# push 1
# push 2
# push 3

# peek 3
# peek 3
# peek 3

# pop 3
# pop 2
# pop 1

class Stack():
   
    def __init__(self, result):
        self.result = result

    def push(self, item):
        self.result.append(item)

    def peek(self):
        length = len(self.result)
        return self.result[length -1]

    def pop(self):
        return self.result.pop()


stack1 = Stack([1,3,5])
stack1 = Stack([])

stack1.push(5)
stack1.push(6)
print(stack1.peek())
stack1.pop()
print(stack1.peek())
