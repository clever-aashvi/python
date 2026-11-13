type = input("Do you want to solve for sin, cos, or tan? (Type in s, c, or t): ")

if type == "s":
    num1 = int(input("Enter your Opposite Side: "))
    num2 = int(input("Enter your Hypotenuse: "))
    print(num1/num2)
if type == "c":
    num3 = int(input("Enter your Adjasent Side: "))
    num4 = int(input("Enter your Hypotenuse: "))
    print(num3/num4)
if type == "t":
    num5 = int(input("Enter your Opposite Side: "))
    num6 = int(input("Enter your Adjasent Side: "))
    print(num5/num6)
