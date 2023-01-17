# WAP TO ACCEPT A NUMBER FROM THE USER AND CHECK WHETHER IT IS ARMSTRONG NUMBER OR NOT.

print("enter the number:")
num=int(input())
print("entered number is",num)
temp=num
s=0
while num>0:
    r=num%10
    s=s+(r*r*r)
    num=int(num/10)

if s==temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

print("This programme is done by 'Farooq Hussain'")