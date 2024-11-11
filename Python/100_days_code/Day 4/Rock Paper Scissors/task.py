import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("""
What do you choose : 
(1) Rock
(2) Paper
(3) Scissor

You choosing : 
"""))

if user == 1 :
    print(rock)
elif user == 2 :
    print(paper)
elif user == 3 :
    print(scissors)
else :
    print("Game over! you didn't choose the options given")
    exit()

computer = random.randint(1,3)

print("Computer Choose : ")

if computer == 1 :
    print(rock)
elif computer == 2 :
    print(paper)
else :
    print(scissors)


user_win_message =  "Result : You Win!"
computer_win_message = "Result : Computer Win!"

if computer == user :
    print("Result : Draw !")
    exit()


if user == 1 :
    if computer == 2 :
        print(computer_win_message)
    else :
        print(user_win_message)
elif user == 2 :
    if computer == 1:
        print(user_win_message)
    else :
        print(computer_win_message)
else :
    if computer == 1:
        print(computer_win_message)
    else :
        print(user_win_message)