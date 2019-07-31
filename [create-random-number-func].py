import random

# Defining between 0 to 100, 6 pieces random numbers

def num_generator(start=0, finish=100, quantity=6):
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randrange(start, finish))
    return numbers
# Printed defined function
print(num_generator())

print("\n")

# Now we can make arrangements our func. We created ten lines from defined func.
for i in range(10):
    print(num_generator())

print("\n")

# Numbers was printed one by one and straight line
print(*num_generator(), sep="-")

print("\n")

# We generated numbers from 0 to 700, 6 pieces.
print(num_generator(0, 700, 10))
