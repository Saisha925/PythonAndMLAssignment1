# 15. Write a program that reads data from a CSV file and prints it to the consel
import csv
f=open("new.csv", mode='w')
cw=csv.writer(f)
lines=[['Organization', 'CEO', 'Established'],
['Alphabet', 'Sundar Pichai', '02-Oct-15'],
['Microsoft', 'Satya Nadella', '04-Apr-75'],
['Amazon', 'Jeff Bezos', '05-Jul-94']]
cw.writerows(lines)
f.close()
f=open("new.csv", mode='r')
cr=csv.reader(f)
for i in cr:
    print(i)
f.close()
