# https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

def main():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    print([num for num in a if num%2 == 0])
main()