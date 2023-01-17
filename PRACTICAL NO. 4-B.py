#Create a program that asks the user to enter their name and their age. Print out a message addressed to them
# that tells them the year that they will turn 100 years old.


name = input("Enter The Name :")
age = int(input("Enter The Age :"))

year = str((2022 - age) + 100)
print(name," You will be 100 years old in the year ",year)
print("this programme is done by 'Farooq Hussain'")