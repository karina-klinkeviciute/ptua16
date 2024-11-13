# Assume a PIN code consists of 4 random digits stored in a variable. We can call it stored_pin.
# Then create a loop going through all possible combinations until you find the one stored.

stored_pin = "0004"
for pin_guess in range(1, 9999):
    pin_guess_str = str(stored_pin)
    while pin_guess < 1000:
        pin_guess_str = f"0{pin_guess_str}"
        pin_guess = pin_guess * 10
    if pin_guess_str == stored_pin:
        print(f"{pin_guess_str} is the correct pin")
        break


for item in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(item)

for index, _ in enumerate([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print(index)

for key, value in {1 : "a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f"}.items():
    print(value)

for _ in range(1, 100):
    print("*", end="")
