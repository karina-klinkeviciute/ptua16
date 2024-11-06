for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, end=" ")

    print("\n")

numbers = [1, 5, 9, 4]

# average = sum(numbers) / len(numbers) if numbers else 0

if numbers:
    average = sum(numbers) / len(numbers)
else:
    average = 0

