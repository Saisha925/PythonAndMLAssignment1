# 6. Write a program that reads the content of a text file and prints it to the console.

f=open("file.txt", 'r')
s=f.read()
print("Content of file: ", s)
f.close()
