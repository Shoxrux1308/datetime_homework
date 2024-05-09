#Task 4:
#Write a Python program that calculates the age of a person based on their birth year. Prompt the user to enter their birth year, and display their current age.
import datetime
a=datetime.date(2005,8,13)
d=datetime.datetime.today()
print(int(d.strftime("%Y"))-a.year)