# 16. Write a program in python that counts the frequency of each character in a string.

s=input("Enter a string: ")
c=0
charfreq={}
for i in s:
    if i not in charfreq:
        charfreq[i]=0
    charfreq[i]+=1
print(charfreq)
