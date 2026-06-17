my_set = {1,2,3}
print(my_set)

my_set = {1.0,"Hello",1,2,3}
print(my_set)

my_set = {1,2,3,4,2}
print(my_set)

my_set = set([1,2,3,2])
print(my_set,"\n")

num_set = set([0,1,3,4,5])
print("The orginal set is")
print(num_set)

num_set.pop()
print("Ater removing the first element from the said set:")
print(num_set)

#Activity2
set_1 = {"Green","Blue"}
set_2 = {"Blue","Yellow"}

print("The original set elements:")
print(set_1)
print(set_2)

print("Intersection of two said sets:")
setz = set_1.intersection(set_2)
print(setz)

#Activity3
import array as arr

array_num = arr.array("i",[1,3,5,3,7,9,3])
print("The original array number:",str(array_num))

print("Number of occurances of the number 3 in the said array:",str(array_num.count(3)))

array_num.reverse()
print("The reverse orders of items")
print(str(array_num))