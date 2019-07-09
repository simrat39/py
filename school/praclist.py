from math import pi,sqrt
from random import randint

choice = 0

while choice != 404:

    choice = int(input("Enter the question number (int)(404 to exit): "))

    if choice == 1:
        radius = eval(input("Enter the radius: "))
        area = math.pi * radius ** 2
        circum = 2 * math.pi * radius
        print("The radius is ",radius,"\nThe area is ",area,"\nThe circumference is ",circum)

    elif choice == 2:
        princ = eval(input("Enter principle amount: "))
        rate = eval(input("Enter rate (per annum %): "))
        time = eval(input("Enter time (years): "))
        si = (princ * rate * time ) / 100
        print("Final amount is:",si+princ,"and interest is:",si)

    elif choice == 3:
        num = eval(input("Enter a number: "))
        print("The sum of first three multiples of",num,"is",num,num*2,num*3)

    elif choice == 4:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        classs = input("Enter your class: ")
        print("Welcome",name)
        print("I am",age,"years old and studying in class",classs)
        print("Lat year I was",age-1,"years old")
    
    elif choice == 5:
        money = int(input("Enter the amount of money: "))
        currency = [[1000,0],[500,0],[100,0],[50,0],[10,0],[5,0],[2,0],[1,0]]
        for i,j in currency:
            if money > 0:
                j = money // i
                money = (money - (j*i))
                print(j,":",i)

    elif choice == 6:
        first_num = eval(input("Enter a number: "))
        second_num = eval(input("Enter another number: "))
        operator = input("Enter operator: ")
        def giveOperator(operator):
            if operator == "+":
                return first_num + second_num
            elif operator == "-":
                return first_num - second_num
            elif operator == "*":
                return first_num * second_num
            elif operator == "/":
                try:
                    div = first_num / second_num
                    return div
                except ZeroDivisionError:
                    print("Cant divide by zero!, Goodbye")
            elif operator == "//":
                return first_num // second_num
            elif operator == "%":
                return first_num % second_num
            elif operator == "**":
                return first_num ** second_num
            else:
                print("Wrong Operator")
        print(first_num,operator,second_num,"=",giveOperator(operator))

    elif choice == 7:
        print("This is not a maths class")
    
    elif choice == 8:

        def isBirthday():
            q = bool(input("Is today your birthday?(True/False): ").capitalize())
            return q

        def giveTicket(speed):
            if not isBirthday():
                if speed <= 60:
                    return 0
                elif speed in range(61,81):
                    return 1
                elif speed >= 81:
                    return 2
            else:
                if speed <= 65:
                    return 0
                elif speed in range(66,86):
                    return 1
                elif speed >= 86:
                    return 2
        print("Your ticket is:",giveTicket(eval(input("Enter your speed (in km/h): "))))
    
    elif choice == 9:
        units = int(input("Enter units used: "))
        temp = units
        cost =0
        if temp <= 100:
            cost += units * .40
        if temp > 100:
            cost += 100 *.40
            units -= 100
            cost += units * .50
        if temp > 300:
            units -= 200
            cost += units * .60
        print(cost + 50)

    elif choice == 10:
        while True:
            try:
                num = int(input("Enter a number please: "))
                break
            except ValueError as e:
                print(e)
                print("Not an integer, please try again")

        def sumOddPosition(num_list):
            sum = 0
            for i in range(0,len(num_list)):
                if i % 2 == 0:
                    sum += num_list[i]
            return sum

        def proEvenPosition(num_list):
            sum2 = 1
            for i in range(1,len(num_list)+1):
                if i % 2 == 0:
                    sum2 *= num_list[i-1]
            return sum2

        num_list = [int(x) for x in str(num)]

        print("The sum of (the sum of digits in even place) and (the product of digits in odd place) is ",sumOddPosition(num_list) + proEvenPosition(num_list))

    elif choice == 11:
        a = [i for i in range(2000,3201) if i % 7 == 0 and i % 5 != 0]
        for i in a:
            print(i,end= ",")
    
    elif choice == 12:
        n = int(input("How many students?"))
        countA,countB,countC,countD = 0,0,0,0
        for i in range(n):
            age = int(input("Enter age: "))
            if age >= 12 and age < 15:
                countA += 1
            elif age >= 15 and age < 17:
                countB += 1
            elif age >= 17 and age < 19:
                countC += 1
            elif age < 12:
                countD += 1

        print("Group A:",countA)
        print("Group B:",countB)
        print("Group C:",countC)
        print("Group D:",countD)

    elif choice == 13:
        num = str(input("Enter ISBN number: "))
        num_list = [int(x) for x in num]
        
        def giveIfLegitISBNnum():
            if len(num_list) != 10:
                return False

            x = 1
            sum = 0

            for i in num_list[0:9]:
                sum += x * i
                x += 1 

            if sum % 11 == num_list[-1]:
                return True
            else:
                return False

        if giveIfLegitISBNnum():
            print("Legit ISBN Number")
        else:
            print("Not an ISBN Number")

    elif choice == 14:
        num = str(input("Enter a number: "))
        if num[::] == num[::-1]:
            print("Number is a palendrome")
        else:
            print("Not a palendrome")
    
    elif choice == 15:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        while True:
            if a > b:
                a = a - b
            elif a < b:
                b = b - a
            if a == b:
                break
        print("HCF is", a)

    elif choice == 16:
        list1 = list(range(1,7))
        list2 = []
        for x in list(range(6,14)):
            x = x - 0.5
            list2.append(x)
        for y,x in zip(list1,list2):
            i = 2 * (y + (0.5 * x))
            print("i =",i,"y =",y,"x =",x,sep=" | ")

    elif choice == 17:
        name = input("Enter your name: ")
        random_num = randint(1,20)
        guess = 0
        while guess < 3:
            user_guess = int(input("Guess a number(1-20): "))
            guess += 1
            if user_guess == random_num:
                print("Good job,",name,"! You guessed my number in",guess,"guesses")
            elif user_guess > random_num:
                print("Too high")
            elif user_guess < random_num:
                print("Too low")
        if guess == 3 and user_guess != random_num:
            print("Sorry, your three turns are over")

    elif choice == 18:
        n = int(input("Give the value of n: "))
        x = int(input("Give the value of x: "))
        aorb = input("Enter question part(a/b): ")
        if aorb == 'a':
            sum = 0
            for denom in range(1,n+1):
                sum += x ** denom / denom
                print(sum)
        elif aorb == 'b':
            sum = 0
            for var in range(1,n+1):
                sum += var / sqrt(var+1)
            print(sum)
        