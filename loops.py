# Example to print numbers from 1 to 5
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

print("loop done")

# while True:
#      a = input("Enter a number: ")
#
#     try:
#         a = int(a)
#         if a:
#             print(f"You entered {a}. {a} squared is {a*a}")
#             break
#     except ValueError:
#         print("Please enter a number")


name = "CodeAcademy"
for character in name:
    print(character)

a_list = [1, 2, 3, 4, 5]
for number in a_list:
    print(number)

names = ["Albert", "Tom", "Leonardo"]
for name in names:
    print(f"Greetings, {name}")

for a in range(1, 11, 2):
    print(a)

n = 20

for a in range(1, n + 1):
    print(a)

n = int(input("Enter a number: "))

for a in range(1, n + 1):
    for b in range(1, a + 1):
        print("*", end="")
    print()

