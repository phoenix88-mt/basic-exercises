# Transition from decimal number to binary, octal, hexadecimal numbers
decimal_number = int(input("Enter number: "))
print("Binary:", "{:b}".format(decimal_number), "or", bin(decimal_number))
print("Octal:", "{:o}".format(decimal_number), "or", oct(decimal_number))
print("Hexadecimal:", "{:x}".format(decimal_number), "or", hex(decimal_number))
