import random


def generatenumbers():
    numbers = []
    while True:
        numbers = [random.randint(1, 25) for numbers in range(4)]
        if sum(numbers) == 26:
            break
    return numbers


for i in range(3):
    random_numbers = generatenumbers()
    print("Random numbers with sum 26 (Invite", i + 1, "):", random_numbers)
