
class Squareroot:
    def __init__(self, num):
        self.ans = 1
        self.num = num

    def calcroot(self):
        while (self.ans ** 2 != self.num):
            self.ans = 0.5 * (self.ans + self.num / self.ans)
        return self.ans


def main():
    number = float(input("Enter number you want to find square root for "))
    sqrt = Squareroot(number)
    ans = sqrt.calcroot()
    print("Answer is ", ans)


if __name__ == "__main__":
    main()
