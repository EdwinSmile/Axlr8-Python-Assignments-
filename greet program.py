name=input("Enter your name: ")
import datetime
time = datetime.datetime.now()
time.hour
if time.hour < 12:
    print ("Good Morning " + name)
elif 12 <= time.hour < 18:
    print ("Good Afternoon " + name)
else:
    print("Good Evening " + name)
