# Conditional

a = 5
b = 5

if a > b :
    print(f"{a} is higher than {b}")
elif a is b :
    print(f"{a} is the same with {b}")
else :
    print(f"{a} is lower then {b}")
    
    
c = input("masukkan nilai c : ")

if a > b and b > c : 
    print(f"{a} higher then {b} and b is higher then {c}")
elif a < b and b > c :
    print(f"{a} is higher then {b}")
elif a > b and b < c :
    print(f"{a} is higher then {b} and {b} is higher then {c}")
else:
    print(f"au ah capek")
    
## Shorthand
print(f"{c} adalah angka ganjil") if int(c) % 2 == 1 else print(f"{c} adalah angka genap")
    
# Loop

## For Loop

for i in range(10) :
    print(f"index-{i}")
    
numbers = [2, 4, 6, 8, 10]

for i in numbers:
    print(f"number-{i}")
    
number = 10

while(number > 0) :
    print(number)
    number -= 1
    
number = 1

while(number < 11) :
    print(f"{number}")
    if(number  is not 5) :
        number += 1
        continue
   
    print(f"this string will show if number is 5")
    
    number += 1