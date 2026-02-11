class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand      
        self.model = model       
        self.speed = speed       

    def accelerate(self, increase):
        self.speed += increase
        print(f"{self.brand} {self.model} accelerated by {increase} km/h. Current speed: {self.speed} km/h")

    def brake(self, decrease):
        self.speed -= decrease
        if self.speed < 0:
            self.speed = 0
        print(f"{self.brand} {self.model} slowed down by {decrease} km/h. Current speed: {self.speed} km/h")

    def status(self):
        print(f"Car: {self.brand} {self.model}, Speed: {self.speed} km/h")


my_car = Car("Toyota", "Corolla")
my_car.status()
my_car.accelerate(30)
my_car.accelerate(20)
my_car.brake(25)
my_car.status()
