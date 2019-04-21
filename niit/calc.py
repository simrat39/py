choice = 0
while choice !=5:
    choice = int(input("Enter your choice: "))
    if choice == 5:
        break
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if choice == 1:
        print(a+b)
    elif choice == 2:
        print(a-b)
    elif choice == 3: 
        print(a*b)
    elif choice == 4:
        try:
            print(a/b)
        except ZeroDivisionError:
            print("Can't divide by zero")