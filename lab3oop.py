
class Polynom:
    def __init__(self, string):
        self.string=string

    def formstring(self):
        polynums = self.string.split(" ")
        return polynums

    def calculate(self, polynums):
        sum=0
        i=0
        while i < len(polynums):
            sum += (1 / int(polynums[i]))
            i +=1
        return sum


def main():
    string = str(input("Enter numbers for polynom divided by whitespaces: "))
    poly = Polynom(string)
    polynums = poly.formstring()
    sum=poly.calculate(polynums)
    print("Answer is ", sum)

    
if __name__ == "__main__":
    main()
