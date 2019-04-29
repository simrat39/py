num = int(input("How many numbers do you want in the fibonacci series: "))

def fibonacci():
    if num == 0:
        a=[]
    elif num == 1:
        a = [0]
    else:
        a = [0,1]
        while len(a) <= (num - 1):
            a.append(a[-1] + a[-2])
    return a

print(fibonacci())