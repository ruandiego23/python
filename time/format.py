import datetime
import time

now = datetime.datetime.now()
print("Current date and time is:")
print("Date: " + now.strftime("%y-%m-%d"), "Time: " + now.strftime("%H:%M:%S"))

print(time.strftime("%H:%M:%S"))
print(time.strftime("%I:%M:%S"))
print(time.strftime("%I:%M:%S %p"))
print(time.strftime("%c"))

date_string = "2018"

print()
print("date_string =", date_string)

date_object = time.strptime(date_string, "%Y")
print("date_object =", date_object)

print()
date_string = "12/11/2018 18:53:32"
date_and_time = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")

print("date_object =", date_and_time)
