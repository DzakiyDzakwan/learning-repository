from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    def __init__(self, model):
        self.model = model
    
    # Abstract Method (Subclasses MUST implement this method)
    @abstractmethod
    def start_engine(self):
        pass

    # Concrete Method (Can be used by subclasses without change)
    def stop_engine(self):
        print(f"The {self.model} engine has been turned off.")

# Concrete Subclass
class Motorcycle(Vehicle):
    # Must implement the abstract method 'start_engine'
    def start_engine(self):
        print(f"The {self.model} engine is started with a kick pedal.")

# Another Concrete Subclass
class Truck(Vehicle):
    # Must implement the abstract method 'start_engine'
    def start_engine(self):
        print(f"The {self.model} engine starts with a strong diesel rumble.")

# vehicle = Vehicle("Generic") # This would raise a TypeError because Vehicle is an ABC!

# Create concrete objects
bike = Motorcycle("Harley-Davidson")
truck = Truck("F-150")

print("--- Abstraction Example ---")
# The user only interacts with the 'start_engine' and 'stop_engine' interface
bike.start_engine()
bike.stop_engine()
print("-" * 15)
truck.start_engine()
truck.stop_engine()