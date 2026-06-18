num_1 = {1,4,6,8}
num_2 = {2,5,7,9}


result = map(lambda x,y:x+y,num_1,num_2)
print("Addition of two lists")
print(list(result))

nums = [1,2,3,4,5]
def sq(n):
    return n*n
square = list(map(sq,nums))
print("The square of number in the list")
print(square)

#Activity2
s1 = {2,3,1}
s2 = {"a","c","b"}
s3 = list(zip(s1,s2))
print(s3,"\n")

list_1 = [10,20,30,40]
list_2 = [100,200,300,400]
for x,y in zip (list_1,list_2[::-1]):
    print(x,y)

stocks = ["Reliance","LuLu","infosis"]
prices = [1225,3335,2775]
new_dict = {stocks:prices for stocks,
            prices in zip(stocks,prices)}
print("\n{}".format(new_dict))

#Activity3
for i in range(10):
    if i == 5:
        print(exit)
        exit()
    print(i)