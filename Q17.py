# 17. Write a program in python that converts a given string to title case (first letter of each word capitalized).

s=input("Enter a string: ")
l=s.split()
new=[]
for i in l:
    i= i.capitalize()
    new.append(i)
print(" ".join(new))
