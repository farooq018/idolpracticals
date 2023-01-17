#Write a function that reverses the user defined value.

def revNum(num):
    rev = 0
    while num > 0:
        r = num % 10
        rev = rev * 10 + r
        num = num // 10
    print("Reverse =",rev)


num = int(input("Enter The Number :"))
revNum(num)
print("this progamme is done by 'Farooq Hussain'")