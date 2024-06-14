# 21. Write a python program that counts the occurrences of a specific element in a list.

l=[]
while True:
    num=int(input("Enter numbers (press 0 to stop) "))
    l.append(num)
    if num==0:
        break
c=0
ele=int(input("enter the element: "))
for i in l:
    if ele == i:
        c+=1
print("The element occurs ", c," times")
