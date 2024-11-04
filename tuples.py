a_list = [1, 2, 3]

print(a_list)

a_list.append(4)

print(a_list)

a_tuple = (1, 2, 3)

print(a_tuple)

a_list[1] = 5

print(a_list)

a_tuple = (1, 2, 3)

# a_tuple[1] = 5

print(a_tuple)

a_tuple = ([4, 5, 6], (1, 2), 3)

a = 15

a_tuple = (a, 2, 5)

a = 7

print(a_tuple)

a_tuple = ([4, 5, 6], (1, 2), 3)

a_tuple[0][1] = 20
print(a_tuple)
a_tuple[0].append(12)
print(a_tuple)
# a_tuple[0] = [4, 20, 6, 12]

a_list = [1, 5, (2, 4)]
print(a_list)

# a_list[2][0] = 5

a_list[2] = (5, 4)
print(a_list)

a_tuple = (1, 5, 6, 7, 9, 12, 54)

print(a_tuple[2:6])
print(a_tuple[::-1])

a_list = list(a_tuple)

a_list[0] = 45

a_tuple = tuple(a_list)

print(a_tuple)
