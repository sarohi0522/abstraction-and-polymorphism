from abc import ABC, abstractmethod

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Dog(Animal):
    def move(self):
        print("I can bark:")

class Lion(Animal):
    def move(self):
        print("I can roar:")

class Snake(Animal):
    def move(self):
        print("I can crawl and hiss:")

obj1 = Human()
obj2 = Dog()
obj3 = Lion()
obj4 = Snake()
obj1.move()
obj2.move()
obj3.move()
obj4.move()

        
