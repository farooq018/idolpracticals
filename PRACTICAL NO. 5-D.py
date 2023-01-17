"""Write a function that takes a character (i.e. a string of
length 1) and returns True if it is a vowel, False otherwise."""


def vowelCheck(ch):
    if ch == "a" or ch == "i" or ch == "o" or ch == "e" or ch == "u" or ch == "A" or ch == "O" or ch == "E" or ch == "U" or ch == "I":
        return True
    else:
        return False


ch = input("Enter the Character :")

ans = vowelCheck(ch)
if ans == True:
    print(ch, " is an Vowel")
else:
    print(ch, " is not an Vowel")

print("This programme is done by'Farooq Hussain'")

