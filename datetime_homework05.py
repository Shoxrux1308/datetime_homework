#Task 5:
#Write a Python program that prompts the user to enter a specific date in the format "dd-mm-yyyy" and determines the day of the week on which that date falls.
import datetime
a=datetime.date(2024,12,31)
print(a.strftime("%A"))