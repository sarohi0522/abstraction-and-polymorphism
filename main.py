from abc import ABC, abstractmethod

class Absclass(ABC):

    def print(self, x):
        print(x)

    @abstractmethod
    def task(self):
        print("We are in the abstract class")

class Subclass(Absclass):
    def task(self):
        print("we are inside the_subclass")


test_obj = Subclass()
test_obj.task()
test_obj.print("Hello world!")
