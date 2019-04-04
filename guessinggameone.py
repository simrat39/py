from random import randint

def main():
    num = randint(1,9)
    user_input = input("Guess a number")
    while user_input != 'exit' and user_input != num:
        if user_input == num:
            print("Correct Guess!")
        elif user_input > num:
            print("Guessed too high!")
        elif user_input < num:
            print("Guessed too low")
        if user_input == 'exit':
            break
        
main()
