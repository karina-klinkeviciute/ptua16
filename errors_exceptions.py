class DataError(Exception):
    pass


print("Hello World")

# a = input("Enter a number")
# b = input("Enter another number")
#
# try:
#     a_number = int(a)
#     b_number = int(b)
#     print(a_number + b_number)
# except ValueError:
#     print("Please enter a number")





def my_dummy_int_func(a: float | str) -> None:
    try:
        int_value = int(a)
        print(f"Result = {int_value}")
    except ValueError:
        print("Value of 'a' cannot be deduced to integer")
    except TypeError:
        print("Type of 'a' is incompatible; it should be either a number or a string")
    except DataError:
        print("Data Error")


my_dummy_int_func("kj")
my_dummy_int_func([1, 2, 3])


def my_dummy_int_func2(a: float | str) -> None:
    try:
        int_value = int(a)
        print(f"Result = {int_value}")
    except (ValueError, TypeError):
        print(f"Value of 'a' ({a}) cannot be deduced to integer")

my_dummy_int_func2("kj")
my_dummy_int_func2([1, 2, 3])


def my_dummy_int_func3(a: float | str) -> None:
    try:
        int_value = int(a)
        print(f"Result = {int_value}")
    except (ValueError, TypeError) as error:
        print(f"Value of 'a' ({a}) cannot be deduced to integer. Error message was: {error.args[0]}")

my_dummy_int_func3("kj")
my_dummy_int_func3([1, 2, 3])


def my_dummy_int_func4(a: int) -> None:
    if a < 0:
        raise ValueError("Negative numbers are not allowed")

    print(f"Result = {a}")


# c = int(input("Enter a number: "))


# try:
#     my_dummy_int_func4(c)
# except ValueError as err:
#     print(f"Something's wrong. Error message:{err}")

def divide_two_numbers(a: int, b: int) -> None:
    try:
        output = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"Output = {output}")
    finally:
        print("Done")


divide_two_numbers(10, 0)

