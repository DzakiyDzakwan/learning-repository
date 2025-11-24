class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"

class Person:
    def speak(self):
        return "Hello!"

# A function that doesn't care about the object's class, only if it has a 'speak()' method
def make_it_speak(entity):
    print(entity.speak())

# Create objects
c = Cat()
d = Duck()
p = Person()

# The function works with all objects because they all implement the 'speak()' method
print("--- Duck Typing ---")
make_it_speak(c)
make_it_speak(d)
make_it_speak(p)