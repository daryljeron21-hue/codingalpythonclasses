x = 6
if (type (x) is int):
    print("true")
else:
    print("false")

x = 6.7
if (type (x) is not float):
    print("true")
else:
    print("false")

#activity2
a = 10
b = -10
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)
a = 5
b = -10
print("a << 1 =", a << 1)
print("b << 1 =", b << 1)

#activity3
#print("please enter your marks")
maths = 80 #int(input())
english = 67 #int(input())
science = 90 #int(input())
social = 80 #int(input())
tamil = 60 #int(input())

sum = maths + english + science + social + tamil
average = sum/5
print(average)

if average >=90:
    print("Grade A")
elif average >=80:
    print("Grade B")
elif average >=60:
    print("Grade C")
else:
    print("Grade D")


