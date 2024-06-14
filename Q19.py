# 19. Write a python program that removes all punctuation from a given string.

s=input("Enter a string: ")
punc=[",",".","!",";",":","?"]
new=""
for i in s:
    if i not in punc:
        new+=i
        
print(new)
