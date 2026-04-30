a = 7
b = 0
c = 3

if a and b and c:
    print("all number has boolean value as true")
else:
    print("atleast 1 number has boolean value as false")

#avtivity2 or-oprator
a = 7
b = 0
c = -3

if a > 0 or b > 0:
    print("either of the number is greater than zero")
else:
    print("no number is greater than zero")

if b > 0 or c > 0:
    print("either of the number is greater than zero")
else:
    print("no number is greater than zero")

#activity3 BMI checker
height = 120 #float(input("please enter your height in cm: "))
weight = 42 #float(input("please enter your weight in kg: "))

BMI = weight / (height/100)**2

print("your BMI height is", BMI)

if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are severely overweight")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("You are severely obese")
