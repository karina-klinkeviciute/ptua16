class Person:

    def __init__(self, name):
        self.name = name


class House:

    location = "Kaunas centre"

    def __init__(self, cost, age, owner: Person = None):
        self.cost = cost
        self.age = age
        self.owner: Person = owner
        print("House created")

    def get_cost(self):
        return f"The cost of the house is {self.cost}"

    def get_age(self):
        return f"The age of the house is {self.age}"

    def compare_cost(self, other):
        if self.cost == other.cost:
            print("The costs of the houses are equal")
        elif self.cost < other.cost:
            print("The cost of the other house is larger")
        else:
            print("The cost of the other house is smaller")


# PycharmProject

print(House(50000, 15))

house = House(55000, 20)

print(house.cost)

house.age = 25

print(house.location)

House.location = "Klaipėda centre"

print(house.location)

print(house.age)

print(type(house))

house1 = House(40000, 50)

house.location = "Vilnius centre"
House.location = "Klaipėda centre"
print(house.location)

print(house1.cost, house1.age)

# print(house1 is house)

house1.cost = 50000

print(house1.location)

print(house1.cost)

print(house.get_age())

print(house1.get_age())

print(house.get_cost())
print(house1.get_cost())

john = Person("John")
jane = Person("Jane")

print(john.name)

house2 = House(77000, 20, owner=john)

print(house2.owner.name)

house2.owner = jane

print(house2.owner.name)

house2.compare_cost(house)
