num = int(input("Enter a number: "))
a = True
for i in range(2,round(num/2)):
    if num/2 % i == 0:
        a = False
if(a):
    print("Number is prime")
else:
    print("Number is not prime")