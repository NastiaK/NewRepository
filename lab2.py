number = float(input("Enter number to find square root for "))
ans = 1.0
prevans=0

while (ans ** 2 != number) & (ans ** 2 != prevans):
    prevans=ans
    ans = 0.5 * (ans + number / ans)

print("Answer is ", ans)
