print("Calculator has started")
while True:
    a = float(input("Enter first number "))
    b = float(input("Enter second number "))
    chooseop=1
    while (chooseop == 1) | (chooseop == 2) | (chooseop == 3) | (chooseop == 4):
        chooseop = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division "))
        print(chooseop)
        if chooseop == 1:
            print(a+b)
            break
        elif chooseop == 2:
            print(a-b)
            break
        elif chooseop == 3:
            print(a*b)
            break
        elif chooseop == 4:
            if b == 0:
                print("Can't divide by zero")
            else:
                print(a/b)
                break
        elif (chooseop != 1) & (chooseop != 2) & (chooseop != 3) & (chooseop != 4):
            print("Invalid operation number")
