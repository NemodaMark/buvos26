def generate_numbers():
    valid_combinations = []
    for num1 in range(1, 26):
        for num2 in range(1, 26):
            for num3 in range(1, 26):
                for num4 in range(1, 26):
                    if num1 + num2 + num3 + num4 == 26:
                        valid_combinations.append([num1, num2, num3, num4])
    return valid_combinations


all_possible_combinations = generate_numbers()

print("All possible combinations with sum 26:")
for i, combo in enumerate(all_possible_combinations, 1):
    print(f"Combination {i}: {combo}")
