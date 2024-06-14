# 18. Write a python program that checks if two strings are anagrams of each other.

s1=input("Enter the first string: ")
s2=input("Enter the second string: ")

if sorted(s1.lower())==sorted(s2.lower()):
    print(s1," and ",s2, " are anagrams")
else:
    print(s1," and ",s2, " are not anagrams")
