n1 = input("enter number1: ") 
n2 = input("enter number2: ")

n1 = int(n1) 
n2 = int(n2)

# negative or positive

if n1 > 0: 
    print(n1, "is positive")
elif n1 < 0: 
    print(n1, "is negative") 
else: 
    print(n1, "is zero")

if n2 > 0: 
    print(n2, "is positive")
elif n2 < 0: 
    print(n2, "is negative") 
else: 
    print(n2, "is zero")
#even or odd

if n1 % 2 == 0: 
    print(n1, "is even")
else: 
    print(n2, "is odd")

if n2 % 2 == 0: 
    print(n1, "is even")
else: 
    print(n2, "is odd")