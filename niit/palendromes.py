a = input("Enter a word to check wheter its a palendorme or not: ")

f = a.lower()

if f == f[::-1]:
    print("Given word is a palendrome")
else:
    print("Given word is not a palendrome")