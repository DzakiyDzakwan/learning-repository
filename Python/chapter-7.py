# Function

def greet() : 
    print("Hello welcome to function course")
    
def greet_parameter(name: str) :
    print(f"Hello {name} welcome to function course")
    
def greet_return() :
    return "Hello this is a return from function"

greet()

greet_parameter("Dzakiy")

print(greet_return())


## Function with many return

def operator(number1:int, number2:int) :
    adition = number1 + number2
    subtraction = number1 - number2
    multiply = number1 * number2
    
    return adition, subtraction, multiply

adition, subtraction, multiply = operator(1, 2)

## *args

def sumarize(*numbers) :
    total = 0
    for number in numbers :
        total += number
        
    return total

print(sumarize(1,3,5,7,9))
print(sumarize(2,4,6,8,10))

## **kwargs
    
def getMember(**member) :
    print(f"welcome {member['name']}, you have been joined this club since {member['year']}")
    
getMember(name = "Dzakiy", year = 2008)

## Lambda

numbers = [1,2,4,5,9,10]

new_numbers = list(filter(lambda number: (number % 2 == 0), numbers))

print(new_numbers)

def myFunction(n) :
    return lambda a : a ** n

doubleFunction = myFunction(2)
tripleFunction = myFunction(3)

print(doubleFunction(4))
print(tripleFunction(4))