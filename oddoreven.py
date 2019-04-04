# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

def main():
    a = float(input("Enter a number: "))
    if a%2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

def extras():
    b = float(input("Enter a another number: "))
    if b%4 == 0:
        print("Number is divisible by 4")
    else:
        print("Number is not divisible by 4")

main()
extras()