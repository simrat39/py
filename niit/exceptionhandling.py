def div(a,b):
    return a/b

while True:
    try:
        num = div(int(input("Enter first number: ")), int(input("Enter second number: ")))
        print("The answer is", num)
        break
    except ZeroDivisionError:
        print("Can't divide by zero, try again")