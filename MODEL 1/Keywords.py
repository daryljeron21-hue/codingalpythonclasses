#Activity_1:
a = "ACADEMEY"
for i in a:
    if(i == "A"):
        print("A is found")
        break
    else:
        print("A is not found")

#Activity_2:
for x in range(10):
    if x % 20 == 0:
        print("Twist")
    elif x % 15 == 0:
        pass
    elif x % 5 == 0:
        print("Fizz")
    elif x % 3 ==0:
        print("Buzz")
    else:
        print(x)

#Activity_3:
num = 5
while num > 0:
    num = num + 1
    if num == 5:
        continue
        print("Found number 5")
