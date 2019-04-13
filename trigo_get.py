import math

def give_cos(a):
    return math.cos(a)

def give_sin(a):
    return math.sin(a)

def give_tan(a):
    return math.tan(a)

def give_cosec(a):
    return 1 / math.sin(a)

def give_sec(a):
    return 1 / math.cos(a)

def give_cot(a):
    return 1 / math.tan(a)

def main():
    a = int(input("Enter the number of which you want to get the value of"))
    lol = raw_input("Enter the trignometric function (cos , sin , tan , cosec , sec , cot) : ")
    yes = lol.lower()
    if yes == "cos":
        print(give_cos(a))
    elif yes == "sin":
        print(give_sin(a))
    elif yes == "tan":
        print(give_tan(a))
    elif yes == "cosec":
        print(give_cosec(a))
    elif yes == "sec":
        print(give_sec(a))
    elif yes == "cot":
        print(give_cot(a))
    else:
        print("Wrong input , try again")
        main()
main()