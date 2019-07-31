import random

def num_generator(start=0, finish=100, quantity=6):
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randrange(start, finish))
    return numbers
print(num_generator())

print("\n")

for i in range(10):
    print(num_generator())

print("\n")

print(*num_generator(), sep="-")

print("\n")

print(num_generator(0, 100, 10))
