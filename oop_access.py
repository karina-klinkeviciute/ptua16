class Employee:
    def __init__(self, name: str, salary: int):
        self._name = name  # Protected attribute
        self.__salary = salary  # Protected attribute

    def tell_name(self):
        print(f"My name is {self._name}")


class HonestEmployee(Employee):
    def tell_salary(self):
        print(f"My salary is {self._Employee__salary}")
        # ^--- OK. Accessing protected attribute within the subclass.


employee1 = Employee("John", 2000)

employee1.tell_name()

employee2 = HonestEmployee("Mary", 5000)

employee2.tell_name()
employee2.tell_salary()

print(employee1._Employee__salary)



class BankAccount:
    def __init__(self, account_holder: str, balance: float = 0.0):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute
        self.__interest_rate = 0.05  # Private attribute

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def apply_interest(self):
        interest = self.__calculate_interest()
        self.__balance += interest
        print(f"Interest of {interest} applied. New balance is {self.__balance}.")

    def __calculate_interest(self) -> float:
        return self.__balance * self.__interest_rate


account = BankAccount("John")

account.deposit(500)

account.withdraw(200)

account.apply_interest()

print(account.get_balance())

print(account._BankAccount__calculate_interest())

print(account._BankAccount__balance)


class Animal:
    def speak(self):
        return "Animal sound"


class Dog(Animal):
    def speak(self):
        return "Bark"


class Cat(Animal):
    def speak(self):
        return "Meow"

class Robot:
    def speak(self):
        return "Beep Beep"


# An object of the class can be created "on the fly",
# without storing it in a variable!
animals = [Dog(), Cat(), Robot()]

for animal in animals:
    print(animal.speak())


def make_noise(entity):
    print(entity.speak())


dog = Dog()
robot = Robot()

make_noise(dog)  # Bark
make_noise(robot)  # Beep Beep



class Calculator:
    def add(self, *args):
        return sum(args)

    def power(self, number, power=2):
        return number ** power


calc = Calculator()

print(calc.add(2, 3))  # 5
print(calc.add(2, 3, 4, 5))  # 14

print(calc.power(5))

print(calc.power(5, 3))



class Combiner:
    def combine(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a + b
        elif isinstance(a, str) and isinstance(b, str):
            return f"{a} {b}"
        else:
            return "Unsupported types for combination."


combiner = Combiner()

# Integer addition
print(combiner.combine(2, 3))  # 5

# String concatenation with a space
print(combiner.combine("Hello", "World"))  # Hello World

# Handling incompatible types
print(combiner.combine(5, "apple"))# Unsupported types for combination.

a = 5
b = 5.0

print(len("something"))

print(len([1, 2, 3]))


