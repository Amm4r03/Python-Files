# inheritance example from class

# create a superclass
class animal:
    name = ""
    def eat(self):
        print("i can eat")
        
# create class, inherit properties from animal
class Dog(animal):
    def display(self):
        print("my name is ", self.name)

# create an object of subclass
labrador = Dog()

labrador.name = "Rohu"
labrador.eat()

labrador.display()