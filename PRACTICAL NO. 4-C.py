#Write a program to generate the Fibonacci series 0 1 1 2 3 5 8 13 21 34 ....
print("This programme is done by 'Farooq Hussain'")
limit = int(input("Enter The Limit of Series :"))

f = 0
s = 1

print(f,end='\t')
print(s,end='\t')

for i in range(3,limit+1):
    n = f + s
    print(n,end="\t")
    f = s
    s = n

