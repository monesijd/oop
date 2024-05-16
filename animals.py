class Animal:
    def __init__(self, color):
        self.color = color

class Dog(Animal):

    def identify(self):
        print(f"This is a {self.color} dog.")

class Cat(Animal):

    def identify(self):
        print(f"THis is a {self.color} cat.")

dog1 = Dog("black")
dog1.identify()
