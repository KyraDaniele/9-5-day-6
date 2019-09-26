class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def print_info(self):
        return("{} {} {}".format(self.year, self.make, self.model))

car = Vehicle('Honda', 'Civic', '2014')
print(car.make, car.model, car.year)
print(car.print_info())