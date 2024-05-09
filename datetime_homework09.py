#Task 9:
#Write a Python program that calculates the difference between two given dates. Prompt the user to enter two dates in the format "dd-mm-yyyy" and display the number of days between them.
import datetime
a=datetime.date(2024,12,23)
b=datetime.date(2024,12,25)
print(abs(int(a.day)-int(b.day)))