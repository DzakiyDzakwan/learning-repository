print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
direction = input('Type "left" or "right, your answer : ').lower()

if not direction == 'left' :
    print("Fall into hole, Game Over!")
    exit()

print("You've come to a lake. There is an island in the middle of the lake")
option = input('Type "wait to wait for a boat. Type "swim" to swim across, your answer : ').lower()

if not option == 'wait' :
    print("Attacked by trout, Game Over!")
    exit()

print('You arrive at the island unharmed. There is a house with 3 doors. Red, Yellow and Blue.')
door = input("Which color do you choose ? your answer : ").lower()

if door == 'red':
    print("Burned by fire, Game Over!")
    exit()
elif door == 'blue':
    print("Eaten by Beast, Game Over!")
    exit()
else:
    print("You win, Congratulation!")
    exit()

