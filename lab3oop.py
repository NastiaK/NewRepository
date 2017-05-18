
class Polynom:
    def __init__(self, string):
        self.string=string

    def formstring(self):
        polynums = self.string.split("--poly=")
        polynums = polynums[1].split(";")
        return polynums

    def calculate(self, polynums):
        sum = 0
        i = 0
        error = 0
        while i < len(polynums):
            try:
                sum += (1 / int(polynums[i]))
                i += 1
            except ValueError:
                error = 1
                i += 1
        if error == 1:
            print("Warning: invalid values are ignored\n")
        return sum


def main():
    string = str(input("Awaiting command: "))
    poly = Polynom(string)
    polynums = poly.formstring()
    sum = poly.calculate(polynums)
    print("Answer is ", sum)

    
if __name__ == "__main__":
    main()
