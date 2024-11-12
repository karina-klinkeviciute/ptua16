from typing import Any

a: int = 1

b: str = "something"

c: float = 1.2

d: bool = True

e: list = [1, 2, 3]

f: list[int] = [1, 2, 3]

g: list[str] = ["a", "b", "c"]

h: list[str] = ["a", "b"]

i: tuple[int, int] = (1, 2)

j: tuple[int, str] = (1, "a")

k: tuple[int, list] = (1, [1, 2, 3])

l: list[int | float] = [1, 1.5]

m: list[int | list[int]] = [1, [2, 3]]

n: tuple[int, list[str]] = (1, ["a", "b", "c"])

o: dict[int, str] = {1: "a", 2: "b", 3: "c"}

p: dict[int, dict[str, int | float]] = {1: {"a": 1, "b": 1, "c": 1}, 2: {"a": 2, "b": 2, "c": 2}}

q = dict[int, Any]


class MyClass:
    pass


r: MyClass = MyClass()


def add(a: int, b: int) -> int:
    return a + b


number = add(1, 2)

print(number)

var: int | None = None

var1: int | None = 1


def the_func(x: int | float, y: tuple[str, str], z: [float | None] = None) -> str:
    return "You called the_func with " + str(x) + str(y) + str(z)


print(the_func(1, ("2", "3")))

