# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

def main():
    a = input("Enter a word to check wheter its a planedorme or not: ")

    if a[::1] == a[::-1]:
        print("Given word is a palendrome")
    else:
        print("Given word is not a palendrome")
main()