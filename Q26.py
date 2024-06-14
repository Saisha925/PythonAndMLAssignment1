#26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.

s=input("Enter a string: ")
prefix=input("Enter the prefix ")
suffix=input("Enter the suffix ")

if s.startswith(prefix) or s.endswith(suffix):
    print("program successful")
else:
    print("prefix and suffix not found")
