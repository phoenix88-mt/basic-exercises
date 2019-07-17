# As you know there are a lot of methods to make calculator in Python
# This calculator will be coded easy method with "eval()"
# But don't forget! when we use eval() method it can be risky -->
# Because we let people to write any code thanks to eval() -->
# That's why we are going to add restraint so that not to write another character except numbers and signs

print("\t".expandtabs(50), "#"*5, "Calculator", "#"*5)
print("""
+ addition
- subtract
/ divide
* multiply
""")

allowed_characters = "1234567890/*-+"
process = input("Enter process(q for quit): ")
while True:
    if process == "q":
        print("closing...")
        break
# We prevented here to enter any code except allowed characters
    for i in process:
        if i not in allowed_characters:
            print("Stop there!")
            quit()
    else:
        data = eval(process)
        print("Result: ", data)
        quit()

