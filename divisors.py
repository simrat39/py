# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

def main():
    num = int(input("Enter a number to get its divisors"))
    x = range(1,num)
    for number in x:
        if num%number == 0:
            print(number)
    
main()