# WAP TO ACCEPT THREE NUMBER FROM THE USER AND DISPLAY THE LARGER NUMBER?

print("Enter your three number:")
n1=int(input())
n2=int(input())
n3=int(input())
if n1<n2 or n1<n3:
    if n2 > n3:
        print(n2,"is Larger number.")
    else:
        print(n3,"is Larger number.")
else:
    print(n1,"is Larger number.")

print("This programme is done by 'Farooq Hussain'")