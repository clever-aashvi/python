
try:
    age = int(input("Please enter your age: "))

    # Check if the age is between 10 and 20 inclusive
    if 10 <= age <= 20:
        print("Your age is between 10 and 20.")
    else:
        print("Your age is not between 10 and 20.")

except ValueError:
    print("Please enter a valid whole number for age.")



