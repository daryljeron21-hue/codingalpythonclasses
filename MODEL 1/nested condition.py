Attendence = 70 #int(input("please enter your attendence:"))
medical_cause = "Y" #int(input("please enter your medical_cause Y/N:"))

if Attendence >=75 or medical_cause == "Y":
    print("You are allowed")
else:
    print("You are not allowed")

#activity2
unit = 125 #int(input("please enter how many unit of electricity is used to know your bill:"))
if unit <=100:
    print("Its free")
elif unit >100 and unit <=200:
    print("Its Rs.5 per unit")
    print("Your electricity bill is", unit*5)
elif unit >200:
    print("Its Rs.10 per unit")
    print("Your electricity bill is", unit*10)
else:
    print("Invalid")
#activity3
print("choose your ride")
print("1.Car")
print("2.Bike")
choice = "Bike" #(input("Enter your choice:"))
if choice == "Bike":
    print("Thanks for purchasing")
elif choice == "Car":
    carchoice = (input("Enter your choice 1.BMW or 2.AUDI:"))
    if Carchoice == "BMW":
        print("Thanks for purchasing")
    elif Carchoice == "AUDI":
        print("Thanks for purchasing")
else:
    print("Invalid choice")