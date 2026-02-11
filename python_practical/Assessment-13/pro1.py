class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")

    def info(self):
        print(f"My name is {self.name}.")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Whiskers")

    dog.info()
    dog.speak()

    print()  

    cat.info()
    cat.speak()
