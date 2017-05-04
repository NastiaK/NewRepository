string = str(input("Enter numbers for polynom divided by whitespaces: "))
polynums = string.split(" ")
sum = 0
i = 0


while i<len(polynums):
    sum += (1 / int(polynums[i]))
    i +=1
print("Answer is ", sum)
