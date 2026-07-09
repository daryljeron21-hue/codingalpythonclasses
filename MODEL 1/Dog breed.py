class Dog:
    def __init__(self,dog,breed):
        
        self.dog = dog
        self.breed = breed

tom = Dog("Tom","pug")
lucky = Dog("Lucky","shih tzu")

print("{} is {} breed".format(tom.dog,tom.breed))
print("{} is {} breed".format(lucky.dog,lucky.breed))