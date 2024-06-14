# 13. Write a program that asks the user for their birth year and calculates their age.

from datetime import date

birth_year = int(input("Enter your birth year: "))

current_date = date.today()

age = current_date.year - birth_year

print("You are", age," years old.")
