def add(name: str, *args, print_this: bool = True) -> int:
    addition = 0
    print(f"counting for {name}")
    for arg in args:
        addition += arg
    if print_this:
        print(addition)
    return addition


print(add("short_list", 1, 2))

# more code


print(add("long_list", 1, 2, 3, 5, 7, 56, print_this=False))


def longest_word(*args, print_this: bool = False) -> str:
    longest_word = ""
    for arg in args:
        if len(arg) > len(longest_word):
            longest_word = arg
    if print_this:
        print(longest_word)

    return longest_word


word = longest_word("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", print_this=True)

print("Word1: ", word)

word = longest_word()

print("Word2: ", word)

def longest_word2(words: list, print_this: bool = False) -> str:
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    if print_this:
        print(longest_word)

    return longest_word


word = longest_word2(["one", "two", "three"], print_this=True)


def add_multiply(multiplier: int, *args, print_this: bool = True) -> int:
    addition = 0
    for arg in args:
        addition += arg
    addition *= multiplier
    if print_this:
        print(addition)
    return addition


result = add_multiply(2, 4, 5, 6, 7, 8, 3, 5, 7, )


def some_function(**kwargs):
    # do something with kwargs
    pass


def do_actions(name: str, *args, height: int = 2, **kwargs) -> None:
    """
    can go forward, backward, left, right
    can also jump or bend
    each action can be done at most once
    """

    print(kwargs)

    x: int = 0
    y: int = 0
    for key, value in kwargs.items():
        if key == "forward":
            y += value
            print(f"{name} moved forward {value} meters")
        elif key == "backward":
            y -= value
            print(f"{name} moved backward {value} meters")
        elif key == "left":
            x -= value
            print(f"{name} moved left {value} meters")
        elif key == "right":
            x += value
            print(f"{name} moved right {value} meters")
        elif key == "jump":
            height += 1
            print(f"{name} jumped {height} meters")
        elif key == "bend":
            height -= 1
            print(f"{name} bended {height} meters")
        else:
            print(f"unrecognized action {key}")

    print(f"{name}'s position is {x}, {y}. It's height is {height} meters")

    some_function(**kwargs)


do_actions("Tom", height=5, forward=1, left=3, jump=True, fly=15, dive=4)

do_actions("Tom")
