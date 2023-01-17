#Write a function to check the input value is Armstrong and also write the function for Palindrome.

# Python code to determine if the provided number is an Armstrong or palindrome.

def armstrong(num):
    sum=0
# find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
# display the result
    if num == sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")

def palindrome(num):
    n = num
    rev = 0
    while(n>0):
        dig = n%10
        rev = rev*10 + dig
        n = n//10
    if num == rev:
        print(num," is palindrome number")
    else:
        print(num," is not a palindrome number")

# take input from the user
num = int(input("Enter a number to check whether it is armstrong or not: "))
armstrong(num)

#take input from the user
num = int(input("\nEnter a number to check whether it is palindrome or not: "))
palindrome(num)

print("This program is done by 'Farooq Hussain'")
