import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_val = input('Enter 0 for Rock 1 for Paper and 2 for Scissors')
comp_val = random.randint(0, 2)
try:
    if int(user_val) == 0 and comp_val == 0:
        print('You chose')
        print(rock)
        print('Computer chose')
        print(rock)
        print('Tie')
    elif int(user_val) == 0 and comp_val == 1:
        print('You chose')
        print(rock)
        print('Computer chose')
        print(paper)
        print('Computer Wins!!')
    elif int(user_val) == 0 and comp_val == 2:
        print('You chose')
        print(rock)
        print('Computer chose')
        print(scissors)
        print('You Win!!')
    elif int(user_val) == 1 and comp_val == 1:
        print('You chose')
        print(paper)
        print('Computer chose')
        print(paper)
        print('Tie')
    elif int(user_val) == 1 and comp_val == 0:
        print('You chose')
        print(paper)
        print('Computer chose')
        print(rock)
        print('You Win!!')
    elif int(user_val) == 1 and comp_val == 2:
        print('You chose')
        print(paper)
        print('Computer chose')
        print(scissors)
        print('Computer Wins!!')
    elif int(user_val) == 2 and comp_val == 2:
        print('You chose')
        print(scissors)
        print('Computer chose')
        print(scissors)
        print('Tie')
    elif int(user_val) == 2 and comp_val == 1:
        print('You chose')
        print(scissors)
        print('Computer chose')
        print(paper)
        print('You Win!!')
    elif int(user_val) == 2 and comp_val == 0:
        print('You chose')
        print(scissors)
        print('Computer chose')
        print(rock)
        print('Computer Wins!!')
    else:
        print('Enter valid value')
except ValueError:
    print('Enter valid input and retry')
