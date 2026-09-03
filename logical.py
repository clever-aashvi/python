# progress to check the appliction of logical not operator

a = 10
b = 12
c = 12

# not is used here to reverce the result of (a == b)
print(not (a == b))

#not is used here to reverce the result of (b==c)
print(not (b == c))

a = 4
b = 5

# not is used here to check that a is not equal to b
if not (a == b):
    print(a, 'and', b, 'are different')

a = 4
b = 5

# not is used here to reverce the result of compairing both conditions
if not ((a == 1) == (b == 5)):
    print ("hello")

a = int(input("enter a number: "))

#not is used here to check that th enumber is not even
if not (a % 2 == 0):
    print(a, "is an odd number.")