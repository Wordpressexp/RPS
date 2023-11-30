import random

print("Hi, Welcome to RPS game!")
print("________________________________")

user_choice = input("Please choose from Rock, Paper, Scissors = ").lower()

print('________________________________')

computer_choice = random.choice(['rock', 'paper', 'scissors'])

if user_choice == computer_choice:
    print('It is a tie')
elif (user_choice == 'rock' and computer_choice == 'scissors') or \
    (user_choice == 'scissors' and computer_choice == 'paper') or \
    (user_choice == 'paper' and computer_choice == 'rock'):
    print('You win this round')
elif (user_choice == 'rock' and computer_choice == 'paper') or \
    (user_choice == 'scissors' and computer_choice == 'rock') or \
    (user_choice == 'paper' and computer_choice == 'scissors'):
    print('Computer wins this round')
else:
    print('Invalid Input')


# if (computer_choice == 'rock'):
#     if (user_choice == 'rock'):
#         print('Computer Choice is = ', computer_choice)
#         print('Rock vs rock is a tie')
#     elif(user_choice == 'paper'):
#         print('Computer Choice is = ', computer_choice)
#         print('User Wins')
#     elif(user_choice == 'scissors'):
#         print('Computer Choice is = ', computer_choice)
#         print('Computer Wins')
#     else:
#         print('Invalid Input')

# if (computer_choice == 'paper'):
#     if (user_choice == 'paper'):
#         print('Computer Choice is = ', computer_choice)
#         print('paper vs paper is a tie')
#     elif(user_choice == 'scissors'):
#         print('Computer Choice is = ', computer_choice)
#         print('User Wins')
#     elif(user_choice == 'rock'):
#         print('Computer Choice is = ', computer_choice)
#         print('Computer Wins')
#     else:
#         print('Invalid Input')


# if (computer_choice == 'scissors'):
#     if (user_choice == 'scissors'):
#         print('Computer Choice is = ', computer_choice)
#         print('scissors vs scissors is a tie')
#     elif(user_choice == 'rock'):
#         print('Computer Choice is = ', computer_choice)
#         print('User Wins')
#     elif(user_choice == 'paper'):
#         print('Computer Choice is = ', computer_choice)
#         print('Computer Wins')
#     else:
#         print('Invalid Input')
