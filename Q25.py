#25. Write a program that copies the contents of one text file to another.

f1=open("read.txt",'r')
f2=open("copy.txt",'w')

s=f1.read()
f2.write(s)

f1.close()
f2.close()
