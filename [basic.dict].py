# Basic Dictionary
import time
phone_book = {"Tom": "1234",
              "John": "1321",
              "Ali": "1112",
              "Jane": "1101"}
person = input("Enter the name for phone numbers: ")
print("Finding...")
time.sleep(0.5)
print("The number of {} is {}".format(phone_book[person], person))
