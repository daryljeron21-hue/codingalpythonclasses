tuplex = ("w",5,"c",6.7,"r",True,"r","o")

print(tuplex)
print(len(tuplex))
print(tuplex.count("r"))
print(tuplex[3:7])
print(tuplex[0:9:27])

#Activity_2
tupley = ("Fruits","Vegetable","Steak","Bread")
print("tuple 1:",tupley)

tuplax = ("Apple","Mango","Avacado","Watermelon")
print("tplw 2:",tuplax)

tuplez = tupley + tuplax
temp = tuplax
tuplax = tupley
temp = tuplax

print(tuplax)
print(tupley)
print(tuplez)

#Activity_3
weather = (0,1,0,1,0,1,1,0,0,1,1)
sunny = 0
raniny = 0
for i in range(0,12):
    if(weather[i] == 1):
        raniny += 1
    else:
        sunny += 1
    if (sunny > raniny):
        print("The weather is good")
    else:
        print("The weather is bad")