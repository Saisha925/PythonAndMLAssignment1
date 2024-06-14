# 14. Write a program that reads multiple lines of input from the user until they enter an empty line,
#then prints all the lines.

lines=[]
while True:
    line=input("Enter a list of lines(press enter to stop)")
    if not line:
        break
    lines.append(line)
print(lines)
