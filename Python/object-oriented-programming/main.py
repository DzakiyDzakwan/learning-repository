class Car():
    is_motorized = True

    # Constructor Method (runs when an object is created)
    def __init__(self, make, model):
        # Instance Attributes (unique to each object)
        self.make = make
        self.model = model
        self.speed = 0

    # Instance Method (behavior)
    def accelerate(self, increment):
        self.speed += increment
        return f"The {self.make} is now traveling at {self.speed} km/h."
    
    #Dunder Method, called when logging the objec
    def __str__(self):
        return f"{self.make} ({self.model})"
    
    def __repr__(self):
        return f"Car(make:{self.make}, model:{self.model})"


# Accessing Class
first_car = Car(make="Toyota", model="Corolla")

#Accessing Object
print(first_car)

# Accessing attributes
print(first_car.make) # Output: Toyota

# Calling a method
print(first_car.accelerate(50)) # Output: The Toyota is now traveling at 50 km/h.