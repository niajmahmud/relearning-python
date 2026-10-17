terminate_program = False
while not terminate_program:
    number1 = input("n1: ")
    number2 = input("n2: ")
    number1 = int(number1)
    number2 = int(number2)


    while True: 
        operation = input("please enter add/sub or quit to exit: ")
        if operation == "quit": 
            terminate_program = True
            break
        if operation not in ["sub", "add"]: 
            print("unknown, try again")
        if operation == "add":
            print("result is ", number1 + number2)
            break; 
        if operation =="sub": 
            print("result is ", number1 - number2)
            break; 5
            