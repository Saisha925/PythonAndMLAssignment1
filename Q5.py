# 5. Write a program that takes a string input from the user and writes it to a text file

f=open("file.txt", 'w')
s=input("Enter a string: ")
f.write(s)
f.close()
