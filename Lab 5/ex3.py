class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency  

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity  

    def calculate_towing_capacity(self):
        return self.towing_capacity

car = Car("Mercedes", "E-class", 2026, 15)
car.display_info()
mileage = car.calculate_mileage(150)
print(f"Estimated mileage for 150 kilometers: {mileage:.2f} liters")

motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2022, 20)
motorcycle.display_info()
mileage = motorcycle.calculate_mileage(150)
print(f"Estimated mileage for 150 kilometers: {mileage:.2f} liters")

truck = Truck("Ford", "F-150", 2022, 5)
truck.display_info()
towing_capacity = truck.calculate_towing_capacity()
print(f"Towing capacity: {towing_capacity} tonnes")
