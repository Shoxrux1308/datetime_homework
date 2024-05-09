#Task 1:
#Write a Python program that displays the current date and time.
import datetime
d=datetime.datetime.now()
print(d.strftime("%d %H:%M:%S"))