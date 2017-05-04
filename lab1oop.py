class Calculations:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        print(self.first + self.second)

    def subtract(self):
        print(self.first - self.second)

    def multiply(self):
        print(self.first * self.second)

    def divide(self):
        if second == 0:
            print("Can't divide by zero")
        else:
            print(self.first / self.second)


def main():
    print("Calculator has started")
    while True:
        a = float(input("Enter first number "))
        b = float(input("Enter second number "))
        chooseop = 1
        calc=Calculations(a, b)
        while (chooseop == 1) | (chooseop == 2) | (chooseop == 3) | (chooseop == 4):
            chooseop = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division "))
            print(chooseop)
            if chooseop == 1:
                calc.add()
                break
            elif chooseop == 2:
                calc.subtract()
                break
            elif chooseop == 3:
                calc.multiply()
                break
            elif chooseop == 4:
                calc.divide()
                break
            elif (chooseop != 1) & (chooseop != 2) & (chooseop != 3) & (chooseop != 4):
                print("Invalid operation number")

if __name__ == "__main__":
    main()
