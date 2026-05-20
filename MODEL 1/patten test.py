print("Half triangle")
num = 7
for i in range(num):
    for j in range(i+1):
        print("*",end =" ")
    print()
print("done")

#Activity-2:
row = 5
number = 1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(number,end =" ")
        number = number + 1
    print()