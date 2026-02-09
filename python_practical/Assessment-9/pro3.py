import random

random_numbers = []

for _ in range(5):
    num = random.randint(1, 100)   
    random_numbers.append(num)

print("Random integers:", random_numbers)
