class Familymember:
    def __init__(self,eye_clour,height_cm):
        
        self.eye_clour = eye_clour
        self.height_cm = height_cm

    def show_traits(self):
        print("The eye colur: ",self.eye_clour)
        print("Height (cm): ",self.height_cm)

class Kid(Familymember):
    def __init__(self, name,age,eye_color,height_cm):
        self.name = name
        self.age = age
        super().__init__(eye_color,height_cm)

    def Show_traits(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        super().show_traits()
    
    def Favourite_hobby(self,hobby):
        print(self.name,"loves",hobby)

child = Kid("Affton",14,"Brown",162)

child.Show_traits()
child.Favourite_hobby("Cycling")

print("Is Kid as a subclass of Familymember",issubclass(Kid,Familymember))