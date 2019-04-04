# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

import random

def main():
    def roll():
        a = random.randint(1,6)
        print("\nrolling dice\n", a)

    def do_again():
        b = input("Do you want to roll again? (y/n)")

        if b == 'y' or b == 'Y':
            main()
        else:
            print("goodbye")

    roll()
    do_again()
main()