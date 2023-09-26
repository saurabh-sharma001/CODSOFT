paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
----.__________)'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
       (____)
---.__(___)   '''

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''


import random
game_images=[rock,paper,scissors]
user_choice=int(input('Enter your choice:\n Type 0 for Rock\n Type 1 for Paper\n Type 2 for Scissors\n'))
if user_choice >= 3 or user_choice < 0:
    print('You entered INVALID choice\n YOU LOSE' )
else:
    print('-------WELCOME TO ROCK PAPER SCISSORS GAME--------')
    print('You chose:')
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print('\n')
    print('Computer Chose:')
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        print('\n')
        print("It's A DRAW")
    elif computer_choice == 0 and user_choice == 2:
        print('\n')
        print('YOU LOSE')
    elif user_choice == 0 and computer_choice == 2:
        print('\n')
        print('YOU WON')
    elif computer_choice > user_choice:
        print('\n')
        print('YOU LOSE')
    elif user_choice > computer_choice:
        print('\n')
        print('YOU WIN')






























                                           
