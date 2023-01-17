#Write a recursive function to print the factorial for a given number.

def fact(x):
    if x == 1 :
        return 1
    else :
        return(x * fact(x-1))

num = int(input("Enter The Number "))
print("Factorial =",fact(num))

print("This programme is done by 'Farooq Hussain'")
