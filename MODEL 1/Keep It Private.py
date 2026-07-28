class myClass:
    __privateVar = 27;

    def privMeth(self):
        print("I'm inside class myClass")
    def Hello(self):
        print("Private variable: ",myClass._privateVar)

foo = myClass()
foo.Hello()
foo._privMeth
