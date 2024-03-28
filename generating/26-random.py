import random

def generate_numbers():
    numbers = []
    while True:
        numbers = [random.randint(1, 25) for i in range(4)]
        if sum(numbers) == 26:
            break
    return numbers

for i in range(3):
    random_numbers = generate_numbers()
    print("Random numbers with sum 26 (Invite", i+1, "):", random_numbers)
