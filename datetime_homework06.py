#Task 6:
#Write a Python program that accepts a date in the format "dd-mm-yyyy" and checks if it is a leap year. Display an appropriate message indicating whether it is a leap year or not.
import datetime
a=datetime.date(2020,12,12)
if (int(a.year)%4==0 and int(a.year)%100!=0) and int(a.year)%400==0 :
    print(True)
else:
    print(False)