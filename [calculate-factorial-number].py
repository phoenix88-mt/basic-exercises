# It's starting for while loops.
print("#"*5, " Factorial Calculator ", "#"*5, sep="")

sum = 1

number = int(input("Enter a number: "))

for x in range(1, number+1):
    sum *= x
    
print(f"Number of factorial {number} is", sum)
