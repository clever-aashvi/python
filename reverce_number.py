number = int(input("Enter your number: "))

digit_count = 0

if number == 0:
    digit_count = 1
else:
    while number > 0:
        number = number // 10
        digit_count += 1

print("Number of digits:", digit_count)
