while True:
    try:
        num = int(input("Enter a number please: "))
        break
    except ValueError as e:
        print(e)
        print("Not an integer, please try again")

def proOddPosition(num_list):
    sum = 1
    for i in range(0,len(num_list)):
        if i % 2 == 0:
            sum *= num_list[i]
    return sum

def sumEvenPosition(num_list):
    sum2 = 0
    for i in range(1,len(num_list)+1):
        if i % 2 == 0:
            sum2 += num_list[i-1]
    return sum2

num_list = [int(x) for x in str(num)]

print("The sum of (the sum of digits in even place) and (the product of digits in odd place) is ",proOddPosition(num_list) + sumEvenPosition(num_list))