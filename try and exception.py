print("Enter  the number1")
num1=(input())
print("Enter the number2")
num2=(input())
try:

    print("the sum of two numbera",int(num1)+int(num2))
except Exception as e:
    print(e)
print("kindly check your input")