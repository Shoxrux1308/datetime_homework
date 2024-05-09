#Task 3:
#Write a Python program that prompts the user to enter a specific date in the format "dd-mm-yyyy" and calculates the number of days between the current date and the entered date.
import datetime
a=datetime.date(2024,12,20)
d=datetime.datetime.today()
print(a.day-d.day)