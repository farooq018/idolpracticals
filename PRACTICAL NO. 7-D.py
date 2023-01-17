#Write the programe to read last n lines of a file.

f=open("xyz.txt",'r')
data=f.read()
print(data)
f.close()