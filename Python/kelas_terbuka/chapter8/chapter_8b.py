def sumarize(*numbers:int):
    total = 0
    for i in numbers:
        total += i
    
    return total

def average(*numbers:int):
    sum = sumarize(numbers)
    
    return sum / len(numbers)
