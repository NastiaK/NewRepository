number = float(input("Enter number you want to find square root for "))
ans = 1.0
prevans=0

while (ans ** 2 != number) & (ans ** 2 != prevans):
    prevans=ans
    ans = 0.5 * (ans + number / ans)

print("Answeris ", ans)
