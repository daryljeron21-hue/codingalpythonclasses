class India():
    def capital(self):
        print("New Delhi is the capital of india")

    def language(self):
        print("Hindi is the most spoken language in india")

    def type(self):
        print("India is a developing country")

class USA():
    def capital(self):
        print("Whashington, D.C is the capital of USA")

    def language(self):
        print("English is the primary language in USA")

    def type(self):
        print("USA is a developed country")

obj_Ind = India()
obj_Usa = USA()

for country in (obj_Ind,obj_Usa):
    country.capital()
    country.language()
    country.type()