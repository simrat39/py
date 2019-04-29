num = int(input("Enter a number to check whether it is armstrong or not: "))
temp = num
sum = 0
while num > 0:
    digit = num%10
    num //= 10
    sum += digit**3

if temp == sum:
    print("Number is armstrong")
else:
    print("Number is not armstrong")