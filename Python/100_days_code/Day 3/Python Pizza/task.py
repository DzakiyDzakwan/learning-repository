print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

total_price:float = 0


if size == 'S':
    total_price += 15
elif size == 'M':
    total_price += 20
elif size == 'L' :
    total_price += 25
else :
    print('You typed wrong inputs!')

if pepperoni == 'Y':
    if size == 'S':
        total_price += 2
    else:
        total_price += 3

if extra_cheese == 'Y': total_price += 1

print(f"Your final bill is: ${total_price}.")