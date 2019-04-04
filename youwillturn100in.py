# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

def main():
    name = str(input("What is your name --> "))
    age = int(input("What is your age --> "))
    year = int(input("What year are you living in --> "))
    year_when_hund = (100 - age) + year
    print(name, "will turn hundred in year", year_when_hund)

main()