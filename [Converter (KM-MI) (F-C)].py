## [Mile-Kilometer] [Celsius-Fahrenheit] Converter ##
print("\t"*10, "#"*4, "Converter", "#"*4, end=" /")
enterance = """Please enter the number you want to do
1 - Kilometers to Miles
2 - Miles to Kilometers
3 - Celsius to Fahrenheit
4 - Fahrenheit to Celsius
"""
print(enterance)
while True:
    operation = input("Please enter the number (q for quit): ")
    if operation == "q":
        print("Exited...")
        break
    elif operation == "1":
        km_to_mile = float(input("Enter km: "))
        print("{} km =".format(km_to_mile), km_to_mile*0.62137, "mile")
        print("\n", enterance, sep="")
    elif operation == "2":
        mile_to_km = float(input("Enter mile: "))
        print("{} miles =".format(mile_to_km), mile_to_km/0.62137, "km")
        print("\n", enterance, sep="")
    elif operation == "3":
        cel_to_fah = float(input("Enter celsius: "))
        print("{} celcius =".format(cel_to_fah), cel_to_fah*1.8+32, "fahrenheit")
        print("\n", enterance, sep="")
    elif operation == "4":
        fah_to_cel = float(input("Enter fahrenheit: "))
        print("{} fahrenheit =".format(fah_to_cel), (fah_to_cel-32)/1.8, "celsius")
        print("\n", enterance, sep="")
    else:
        print("\n", "Please select only numbers between 1-4!!!", sep="")
        print("\n", enterance, sep="") 
