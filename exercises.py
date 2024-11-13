
# Create a function that checks if every letter from a given list of
# letters can be found at least once in a provided list of words.

# Condition: every letter at least once
def can_find(letters: list[str], words: list[str]) -> bool:
    for letter in letters:
        letter_found = False
        for word in words:
            if letter in word:
                letter_found = True
        if not letter_found:
            return False
    return True




# this should return True
print(can_find(["a", "b", "t", "u"], ["beautiful", "the", "hat"]))

print(can_find(["a", "b", "t", "u"], []))

print(can_find(["a", "b", "t", "k"], ["beautiful", "the", "hat"]))

# Condition: all letters at least once in any of the words


def can_find2(letters, words):
    return all(any(letter in word for word in words) for letter in letters)

