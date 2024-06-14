# 11. Write a python program that generates the first n numbers in the Fibonacci sequence.

n=int(input("enter the value of n: "))
a,b=0,1
for i in range(n):
    print(a)
    a,b=b,a+b
