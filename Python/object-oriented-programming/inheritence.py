# Parent Class (Superclass)
class Vehicle:
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels
    
    # Parent's implementation
    def display_info(self):
        print(f"Vehicle: Color={self.color}, Wheels={self.wheels}")

# Child Class (Subclass)
class Car(Vehicle):
    def __init__(self, color, engine_type):
        # Initialize parent attributes
        super().__init__(color, wheels=4)
        self.engine_type = engine_type
    
    # Child's implementation (Overriding the parent method)
    def display_info(self):
        # We can call the parent's method using super() if we want to include its logic
        # super().display_info()
        print(f"Car: Color={self.color}, Wheels={self.wheels}, Engine={self.engine_type}")

# Test the classes
parent_obj = Vehicle("Red", 2)
child_obj = Car("Blue", "Electric")

parent_obj.display_info() # Calls Vehicle's display_info
child_obj.display_info()  # Calls Car's (overridden) display_info