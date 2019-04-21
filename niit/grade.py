def marks():
    inp = int(input("Enter your marks: "))
    if inp in range(0,40):
        print("Fail")
    elif inp in range(41,55):
        print("Grade C - Average")
    elif inp in range(56,70):
        print("Grade B - Good")
    elif inp in range(71,85):
        print("Grade A- - Excellent")
    elif inp in range(86,100):
        print("Grade A - Extraordinary")
    else:
        print("Wrong input, please try again")
        marks()
marks()