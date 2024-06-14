#24. Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) 
#as input and print the result.

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
op=input("Enter the operator from (+, -, *, /): ")

if op=='+':
    print("Sum of the numbers is ", num1+num2)
elif op=='-':
    print("Difference of the numbers is ", num1-num2)
elif op=='*':
    print("Product of the numbers is ", num1*num2)
elif op=='/':
    print("Quotient of the numbers is ", num1/num2)
else:
    print("invalid operator")
