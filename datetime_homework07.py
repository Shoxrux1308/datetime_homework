#Task 7:
#Write a Python program that adds 5 days to the current date and displays the resulting date.
import datetime
a=datetime.date(2024,12,12)
b=int(a.day)+5
print(datetime.date(2024,12,b))