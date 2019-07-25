# To find prime numbers until entered number
prime_num = []
number = int(input("Enter number: "))
for i in range(2, number+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_num.append(i)

for i in prime_num:
    print(i)
print("\nThere are total {} numbers from 0 to {}".format(len(prime_num), number))
