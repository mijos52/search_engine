# instance and class variable


class Car:
    wheels = 4

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


new_car = Car("Ferrari", "2020")

print(new_car.brand)

print(new_car.wheels)
