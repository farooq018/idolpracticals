print("Welcone to Pattern exercise")
print("Enter your number")
num1=int(input())
print("type 1 or 0,1 is for True and 0 is for False")
num2=int(input("Enter your number"))
if num2==True:
    for i in range(0,num1+1):
        print("* "*i)
if num2==False:
    for i in range(num1,0,-1):
        print("* "*i)




