number_one = 500
number_two = 600

if number_one > number_two:
    print("The first number is greater than the second!")
elif number_one == number_two:
    print("Numbers are equal!")
else:
    print("The second number is greater than the first!")

print("number_one is larger") if number_one > number_two else print("number_two is larger or equal")

print("number_one is larger") if number_one > number_two else print("numbers are equal") if number_one == number_two else print("numbers are equal")

persons_apartment = 5

if persons_apartment == 1 or persons_apartment == 2 or persons_apartment == 3:
    print("The apartment is on the ground floor!")
elif persons_apartment == 4 or persons_apartment == 5 or persons_apartment == 6:
    print("The apartment is on the first floor!")
elif persons_apartment == 7 or persons_apartment == 8 or persons_apartment == 9:
    print("The apartment is on the second floor!")
elif persons_apartment == 10 or persons_apartment == 11 or persons_apartment == 12:
    print("The apartment is on the third floor!")
else:
    print("The person doesn't live at this building")


a = 200
b = 400
c = 500

if c > a and c > b:
    print("C is the greatest of them all!")

if b > a or b > c:
    print("B is at least greater than one of the values!")

if c > a and not c <= b:
    print("C is the greatest of them all!")

a = input("Enter a number: ")

# if a == "":
#     print("You did not enter a number")

if not a:
    print("You did not enter a number")

# if len(a) == 0:
#     print("You did not enter a number")

elif not int(a) < 0:
    print("number is positive")

x = 25

if x > 10:
    print("Above 10 ")
    if x > 20:
        pass
        # print("and above 20!")
    else:
        print("but bellow 20!")


name = "Tom"

if name == "Tom":
    print("Nice to see you, Tom!")
else:
    print("Welcome, user!")

s1 = "Z"

s2 = "a"

s3 = "abe"

if s1 > s2:
    print(s1)
else:
    print(s2)

if s2 != "c":
    print("not c")

if not s2 == "c":
    print("not c")


def check_positive(number):
    """check if number is positive"""
    if number >= 0:
        # if it's more than zero or zero, it's cosidered positive
        return True
    return False


def check_negative(number):
    if number < 0:
        return True
    return False