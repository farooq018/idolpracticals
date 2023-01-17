# write a programme to accept two number from the user and swap the number
# a: with using third variable.
# b: without using third variable.

#programme with third variable.
print("Enter your two number:")
n1=int(input())
n2=int(input())
print("number before swapping:")
print("n1=",n1)
print("n2=",n2)

n3=n1
n1=n2
n2=n3
print("number after swapping")
print("n1=",n1)
print("n2=",n2)

#programme without third variable.
print("enter two number:")
n1=int(input())
n2=int(input())
print("numbers before swapping")
print("n1=",n1)
print("n2=",n2)

n1=n1+n2
n2=n1-n2
n1=n1-n2

print("number after swapping")
print("n1=",n1)
print("n2=",n2)

print("This programme is done by 'Farooq Hussain'")