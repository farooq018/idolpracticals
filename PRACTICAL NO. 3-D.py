# WAP TO ACCEPT A NUMBER FROM THE USER AND DISPLAY THE REVERSE AND SUM OF DIGITS OF THAT NUMBER.

print("enter the number:")
num=int(input())
print("Entered number is",num)
rev=0
sod=0
while num>0:
    r=num%10
    rev=rev*10+r
    sod=sod+r
    num=int(num/10)

print("Reverse=",rev)
print("Sum of Digits:",sod)

print("This programme is done by 'Farooq Hussain'")