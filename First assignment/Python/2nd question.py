count = 0
multiply = 1
integer = int(input("Enter the integer for which you want calculate factorial = "))
if integer < 0:
    while integer < 0:
        integer = int(input("The integer must be > or = to 0 = "))
        backup = integer
while (integer > 0):
    multiply =multiply*integer
    integer=integer-1
print("The factorial of",backup,"is =",multiply)
