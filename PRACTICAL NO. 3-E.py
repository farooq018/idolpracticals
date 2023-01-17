# WAP TO ACCEPT A NUMBER FROM THE USER AND CHECK WHETHER IT IS PALLINDROM NUMBER OR NOT.

print("enter the number:")
num=int(input())
temp=num
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print(temp,"is a pallindrom number")
else:
    print(temp,"is not a pallindrom number")

print("This programme is done by 'Farooq Hussain'")