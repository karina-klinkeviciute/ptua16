import random

#     Guess the number (1-10): 5
# Too low! Try again.
# Guess the number (1-10): 8
# Correct! The number was 8.

#     Create a number-guessing game where the computer randomly selects an integer number between 1 and 10.
#     The user is given the chance to guess the number. Inform the user if their guess is correct, too high,
#     or too low.

while True:
    random_number = random.randint(1, 10)

    while True:
        users_number = int(input("Please enter a number between 1 and 10: "))

        if users_number == random_number:
            print(f"Correct! The number was {random_number}")
            break
        elif users_number > random_number:
            print(f"Too high! Try again.")
        else:
            print(f"Too low! Try again.")

    play_again = input("Would you like to play again? (y/n): ")
    if play_again == "n":
        break
