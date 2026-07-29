class Car:
    def __init__(self,car_clour,car_seats):
        self.car_clour = car_clour
        self.car_seats = car_seats

    def show_traits(self):
        print("The car clour: ",self.car_clour)
        print("The number of seats: ",self.car_seats)

class child_car(Car):
    def __init__(self, car_clour, car_seats,car_speed,car_age):
        self.car_speed = car_speed
        self.car_age = car_age
        super().__init__(car_clour, car_seats)

        def Show_traits(self):
                print("The Car speed: ",self.car_speed)
                print("The Cars age: ",self.car_age)
                super().show_traits()