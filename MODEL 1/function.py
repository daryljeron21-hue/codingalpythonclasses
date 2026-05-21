def well_wishes():
    print("Hello")
    print("How are you?")
well_wishes()

#Activity2
def weather():
    print("The weather is great in",spring)
    print("The weather is same in",autum)
spring = "autum"
autum = spring
weather()

#Activity3
def add(P,Q):
    return P+Q
def subract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def divide(P,Q):
    return P/Q

print("Please select the opration")
print("a.Addition")
print("b.Subraction")
print("c.Multiplication")
print("d.Division")

choice = "a"
num_1 = 21
num_2 = 46

if choice == "a":
    print(num_1,"+",num_2,"=",add(num_1,num_2))
elif choice == "b":
    print(num_1,"-",num_2,"=",subract(num_1,num_2))
elif choice == "c":
    print(num_1,"*",num_2,"=",multiply(num_1,num_2))
elif choice == "d":
    print(num_1,"/",num_2,"=",divide(num_1,num_2))
else:
    print("Invalid input")