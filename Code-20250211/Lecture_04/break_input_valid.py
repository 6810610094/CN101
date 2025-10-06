#age = int(input("Enter your age (age >= 0): "))
#while age < 0:
#    print("Error: invalid age.")
#    age = int(input("Enter your age (age >= 0): "))
#print(f"Your age is {age}.")

while True:
    age = int(input("Enter your age (age >= 0): "))
    if age >= 0:
        break
    print()