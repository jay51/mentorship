
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
    url_parts = url.split(':')
    http = url_parts[0]

    u = url_parts[1]
    u = u[2:]
    domain = u.split('/')[0]
    dn = domain[0:len(domain) - 4]
    ext = domain[len(domain) - 4 : ]
    # print(dn)
    # print(ext)

    result = [http, dn, ext]
    return result
    # print(domain)




# url = "https://facebook.com/search?q=cats&tbm=isch"
# print(extract_url(url)) # ['https', 'www.google', 'com']

