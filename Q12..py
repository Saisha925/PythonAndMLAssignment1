# 12. Write a python program that calculates the sum of the digits of a given number

n=int(input("enter a number: "))
length=len(str(n))
sum=0
for i in range (length):
    rem=n%10
    sum+=rem
    n=n//10
print(sum)
