string = "jeron"
char = "n"
count = 0
i = 0

while i < len(string):
    if string (i) == char:
        count += 1
        i += 1
    print("The character", char,"occcurs",count,"times in the",string)

#activity2
lower = 5
upper = 7

for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2,num):
            if num % 1 == 0:
                break
            else:
                print(num)

#activity3
num = 5
t = num
numLen = 0

while t > 0:
    numLen = numLen + 1
    t = int(t/10)
if numLen >= 4:
    numLen = int(numLen/2)
    chk = 0
    while num >0:
        rem = num % 10
        if chk == numLen:
            midone = rem
        elif chk == (numLen -1):
            midtwo = rem
        num = int(num/100)
        chk = chk +1
    prod = midone * midtwo
    print("\nproduct")