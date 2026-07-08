class student:
    grade = 8
    print("hi i am a student of grade",grade)

op = student()


#activity3
classlass parrot:
    species = 'bird'

    def __init__(self,name,age):
        self.name = name
        self.age = age

blu = parrot("Blue",10)
woo = parrot("Woo",15)

print("Blu is a {}",format(blu.species))
print("Woo is a {}",format(woo.species))

print("{} is {} years old"format(blu.name,blu.age))
print("{} is {} years old"format(woo.name,woo.age))

