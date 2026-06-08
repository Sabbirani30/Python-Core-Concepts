Likhon=100
Sabbir=200
Anik=300

if Likhon>Sabbir:
    print("Anik is greater than Sabbir")
elif Anik>Sabbir:
    print("Anik is less than Sabbir")
else:
    print("Anik is equal to Sabbir")


Likhon=1000
Sabbir=200
Anik=3000

if Likhon>Sabbir:
    print("Anik is greater than Sabbir")
    print("Anik is less than Sabbir")
    print("Anik is equal to Sabbir")
elif Sabbir>Likhon:
    print("Sabbir is greater than Sabbir")
    print("Sabbir is less than Sabbir")
    print("Sabbir is equal to Sabbir")
else:
    print("Sabbir is equal to Sabbir")
    print("Sabbir is less than Sabbir")
    print("Sabbir is equal to Sabbir")


#_Grade_Calculator:
Marks= int (input("Enter Marks: "))
if Marks>=80:
    print("A+")
elif Marks>=70:
    print("A")
elif Marks>=60:
    print("A-")
elif Marks>=50:
    print("B")
elif Marks>=40:
    print("B-")
elif Marks>=33:
    print("C")
else:
    print("F")

#Notification_System

notification = int(input("Enter Days left: "))

if notification >= 30:
    print("Your data is active and running smoothly.")
elif notification >= 25:
    print("Your data is almost finished, please recharge soon.")
elif notification >= 20:
    print("Your data is about to run out.")
elif notification >= 15:
    print("Half of your package validity is over.")
else:
    print("Your data is over or ending soon.")












