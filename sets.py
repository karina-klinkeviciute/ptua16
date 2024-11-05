a_set = {8, 5, "hi"}

print(a_set)

a_set.add(7)
print(a_set)

a_set.add(5)

print(a_set)

a_list = [1, 2, 3, 1, 3]

a_set = set(a_list)
print(a_set)

for item in a_set:
    print(item)

print(1 in a_set)

a_set.add(5)

print(a_set)

a_set.remove(5)

print(a_set)

print(a_set.pop())
print(a_set)

a_set.discard(7)
print(a_set)

new_list = [4, 7, 9]

a_set.update(new_list)
print(a_set)

set_a = {1, 2, 3, 4, 5}

set_b = {3, 4, 5, 6, 7}

set_c = set_a | set_b
set_d = set_a.union(set_b)

print(set_c)

set_c = set_a & set_b
print(set_c)

set_c = set_a - set_b
print(set_c)

set_c = set_a ^ set_b
print(set_c)

a_set = {(2, 5), 6, 12, "string here", 2.25}
print(a_set)

a_dictionary = {"a": (1, 2, 4, "a"), }

a_list = [1, 2, 2, 3, 1, 2, 1]

if 1 in a_list:
    print("exists")

a_set = set(a_list)
if 1 in a_set:
    print("exists")
