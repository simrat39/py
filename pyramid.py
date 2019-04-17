n = int(input("How many numbers do you want in the pyramid: "))
assert n >= 0, "Pyramid cant be -ve"
i = 0
while i <= n:
    print(str(i) * i)
    i += 1