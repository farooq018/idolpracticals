# Write a python programee to append text to a file and display the text.

f=open("xyz.txt",'a+')
f.write("  \nThis programe is done by'Farooq Hussain'")
f.close()
f=open("xyz.txt",'r')
data=f.read()
print(data)
f.close()