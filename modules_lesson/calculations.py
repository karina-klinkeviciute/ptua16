# import arithmetics as arithm
from arithmetics import add as arithm_add
from arithmetics import sub

from my_dictionary import my_dict

print(my_dict)


def add(x, y):
    return x * x + y * y


a = 15

b = 22

c = add(a, b)

e = arithm_add(a, b)

# e = arithmetics.add(a, b)

print(c)

print(e)

# d = arithmetics.sub(a, b)

# print(d)
