#Task 8:
#Write a Python program that subtracts 10 hours from the current time and displays the resulting time.
import datetime
a=datetime.datetime.now()
print(datetime.time(int(a.strftime("%H"))-10,int(a.strftime("%M")),int(a.strftime("%M"))))