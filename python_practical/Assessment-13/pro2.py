class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start(self):
        print(f"The {self.brand} vehicle is starting.")

    def info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)  
        self.doors = doors

    def info(self):
        super().info()
        print(f"Doors: {self.doors}")

    def drive(self):
        print(f"The {self.brand} car is driving.")


class ElectricCar(Car):
    def __init__(self, brand, year, doors, battery_capacity):
        super().__init__(brand, year, doors)  
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"The {self.brand} electric car is charging.")

    def info(self):
        super().info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")


# Main program
if __name__ == "__main__":
    vehicle = Vehicle("Generic", 2020)
    car = Car("Toyota", 2022, 4)
    electric_car = ElectricCar("Tesla", 2023, 4, 75)

    print("Vehicle Info:")
    vehicle.info()
    vehicle.start()

    print("\nCar Info:")
    car.info()
    car.start()
    car.drive()

    print("\nElectric Car Info:")
    electric_car.info()
    electric_car.start()
    electric_car.drive()
    electric_car.charge()
