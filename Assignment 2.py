#Question 1
# Base class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"The {self.name} is moving."

# Subclass Car
class Car(Vehicle):
    def move(self):
        return f"The car '{self.name}' drives on the road."

# Subclass Bike
class Bike(Vehicle):
    def move(self):
        return f"The bike '{self.name}' pedals along the path."




#Question 2
# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area method.")

# Subclass Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Subclass Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Function to calculate total area of any shapes
def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()   # Polymorphism at work
    return total


# Example usage
shapes = [Square(4), Rectangle(5, 3), Square(2)]
print("Total area:", total_area(shapes))

# Example usage
v = Vehicle("Generic Vehicle")
c = Car("Toyota")
b = Bike("Mountain Bike")

print(v.move())  # Calls Vehicle's method
print(c.move())  # Calls Car's overridden method
print(b.move())  # Calls Bike's overridden method



#Question 3
# Base class
class Shape:
    def __init__(self, name):
        self.name = name
        print(f"Initializing Shape: {self.name}")

    def calculate_area(self):
        # Base implementation (does nothing meaningful)
        print("Shape.calculate_area() called (base method - no area calculated)")
        return 0


# Derived class
class Rectangle(Shape):
    def __init__(self, name, length, width):
        # Call Shape's constructor
        super().__init__(name)
        self.length = length
        self.width = width

    def calculate_area(self):
        # Call the base class method (even if it does nothing)
        super().calculate_area()
        # Rectangle's specific implementation
        area = self.length * self.width
        print(f"The area of rectangle '{self.name}' is {area}")
        return area


# Example usage
rect = Rectangle("MyRectangle", 5, 3)
area = rect.calculate_area()
print("Returned area:", area)



#Question 4
# Base class
class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement make_sound().")


# Derived class Dog
class Dog(Animal):
    def make_sound(self):
        return "Woof!"


# Derived class Cat
class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Function that works with any Animal
def process_sound(animal):
    # Polymorphism: we don’t care if it's a Dog, Cat, or any other Animal
    print(f"The animal says: {animal.make_sound()}")


# Example usage
dog = Dog()
cat = Cat()

process_sound(dog)  # The animal says: Woof!
process_sound(cat)  # The animal says: Meow!



#Question 5
from abc import ABC, abstractmethod

# Abstract Base Class
class FileHandler(ABC):
    @abstractmethod
    def read(self):
        """Read data from the file"""
        pass

    @abstractmethod
    def write(self, data):
        """Write data to the file"""
        pass


# Concrete class for handling text files
class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            return f.read()

    def write(self, data):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(data)
        print(f"Written text data to {self.filename}")


# Concrete class for handling binary files
class BinaryFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, "rb") as f:
            return f.read()

    def write(self, data):
        with open(self.filename, "wb") as f:
            f.write(data)
        print(f"Written binary data to {self.filename}")




