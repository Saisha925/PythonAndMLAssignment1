# 20. Write a python program that takes a list of numbers and returns their sum.
l=[]
while True:
    num=int(input("Enter numbers (press 0 to stop) "))
    l.append(num)
    if num==0:
        break
for i in l:
    sum+=i
print(sum)
