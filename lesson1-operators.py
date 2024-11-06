print("Hello, group")
a = 5.5
b = 25.3
a2 = 6.2
a2_1 = 7
my_name = "Karina"
print(my_name)
my_name = "Karina Klinkevičiūtė"
print(my_name)

print(type(a))
print(type(a2))
print(type(my_name))

print(a+b)

print(a+b)

print("hello " + my_name)

c = a + b
print(c)

c = a - b
print(c)

c = a * b
print(c)

c = a / b
print(c)

c = a ** b
print(c)

c = a // b
print(c)

c = a % b

print(c)

letter = "a"

new_name = "Code academy!!!"

print(new_name[0])

print(new_name[1])

print(new_name[4])

print(new_name[-1])
print(new_name[-2])
print(new_name[5:12])

print(new_name[5:])

print(new_name[:5])

print(new_name[1:12:2])

print(new_name[5::2])

print(new_name[::-1])

print(new_name.split())

print(new_name.upper())
print(new_name.lower())
print(new_name.title())

print(new_name.replace("C", "k"))

print(new_name.replace("Code", "Music"))

word1 = "Code"

word2 = "Academy"

phrase = word1 + " " + word2
print(phrase)

# This way is the best
phrase = f"Welcome to {word1} {word2}!"
print(phrase)

print(word1, word2)
print(a, b, c)

phrase = "Welcome to {} {}".format(word1, word2)
print(phrase)
phrase = "Welcome to {1} {0}".format(word1, word2)
print(phrase)

phrase = "Welcome to %s %s" % (word1, word2)

print(phrase)

var1 = "45"
var2 = "25"

var1_number = int(var1)
var2_number = int(var2)

var3 = var1 + var2
var3_number = var1_number + var2_number
print(var3)
print(var3_number)  # this is a comment

var1_float = float(var1)
print(var1_float)

# we can't turn str with letters into int
# int("some text")

print(str(5) + str(7))

