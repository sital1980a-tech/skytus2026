class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor called")

    def speak(self):
        print("Animal makes a sound")


# Child Class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print("Dog constructor called")

    def speak(self):
    
        super().speak()
        print(f"{self.name} barks")


# -------- Testing --------

dog1 = Dog("Buddy", "Golden Retriever")

print("\nCalling speak method:")
dog1.speak()
