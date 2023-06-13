

obj = {

    'name':'jack',
    'age': 28,
    'desc': None,
    'info': {
        'hair': 'brown',
        'height': None,
        'charctor': {
            'key': 'value',
            'key2': None
        }
    }
}


def strip_nulls(obj):
    keys = list(obj.keys())

    for key in keys:
        if type(obj[key]) == dict:
            strip_nulls(obj[key])
        
        if obj[key] == None:
            del obj[key]

    return obj

print(strip_nulls(obj))