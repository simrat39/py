def giveCube(x):
    return x**3

num = int(input("Enter a number to check if its armstrong or not: "))
list_num = list(map(int, str(num)))
cube_list = [giveCube(x) for x in list_num]
if sum(cube_list) == num:
    print("Given number is an Armstrong number")
else:
    print("Given number is not an Armstrong number")