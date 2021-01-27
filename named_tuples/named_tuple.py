from collections import namedtuple

class Car(object):
    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model

car = Car("Black", "Ford", "Mustange")

tup = (1, True, object(), -1)
print(tup[0])
print(tup[1])

Car = namedtuple("Car", "color make model mileage")
print(car)

Car = namedtuple("Car", ["color", "make", "model", "mileage"])
print(car)

print(Car("blue", "Tesla", "Model Y", 5))

my_car = Car(color="midnight silver", make="Tesla", model="Model Y", mileage=5)
print(my_car)

my_car.model = "x"
