name = input("Hello! Please enter your name: ")
print("Hello ", name)
print("This sumulation will tell you if your number is an Armstrong number.")
num = int(input("Enter a number:"))
sum = 0
temp = num
while temp > 0:
    digit = temp %10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num ,"is an Armstrong number")
else:
    print(num ,"is not an Armstrong number")