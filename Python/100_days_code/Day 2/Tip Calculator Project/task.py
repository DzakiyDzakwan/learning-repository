print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
total_tip = bill * tip_percentage
total_bill = bill + total_tip

tip_pay = round( total_bill / people , 2)

print(f"Your tip is : {total_tip}")
print(f"Total Bill : {total_bill}")
print(f"Each person should pay: ${tip_pay}")
