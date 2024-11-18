from pprint import pprint

# if __name__ == "__main__":

a_dict = {'a': 1, 'b': 45, 'c': 3}

print(a_dict['a'])

print(a_dict['b'])

a_dict['a'] = 15

print(a_dict)

a_dict[''] = 45
print(a_dict)

a_dict['a'] = 37

print(a_dict)

a_dict[5] = 16
print(a_dict)

a_dict[(1, 2)] = "hi"

print(a_dict)

a_dict = {'a': 1, 2: 45, 'c': "something", '8': [1, 4], "dictionary": {"one": 1, "two": 2, "three": 3}}

print(a_dict)

print(a_dict['a'])

print(a_dict.get('a', "doesn't exist"))

# print(a_dict["b"])

print(a_dict.get('b'))

print(a_dict.get('b', "doesn't exist"))

print(a_dict.get('b', 100))

item = a_dict.pop('8')
print(item)
print(a_dict)

del a_dict['c']

print(a_dict)

user_info = {
"name": "Albert",
"surname": "Einstein",
"occupation": {
   "role": "Professor",
   "workplaces": ["University of Berlin", "University of Washington"]

},
"languages": ["German", "Latin", "Italian", ("English", "British"), ("English", "American"), "French"],
}

# for language in user_info['languages']:
# print(language)
#
# print(user_info["occupation"]["role"])
#
# for a in a_dict:
# print(a)
#
# for a in a_dict.values():
# print(a)
#
# for a in a_dict.keys():
# print(a)
#
# for key, value in a_dict.items():
# print(f"value for {key} is {value}")

a_dict.update(user_info)

pprint(a_dict)

ages_dictionary = {"John": 25, "Jane": 50, "Thomas": 22}

new_ages = {"Peter": 24, "Anna": 45, "John": 35}

ages_dictionary.update(new_ages)

pprint(ages_dictionary)

test_keys = ["Albert", "Tom", "Stephen"]

test_values = [1, 4, 5]

test_dict = dict(zip(test_keys, test_values))
print(test_dict)
