# Playing Rock, Paper, Scissiors game in a loop


import random
list = ['rock', 'paper', 'scissors']
var = 1
while(var == 1):
    random.shuffle(list)
    player1_choice = int(input('Enter Player1 Choice: 0,1,2: '))
    if(player1_choice >= 3):
        while(player1_choice >= 3):
            player1_choice = int(input('Enter Player1 Choice: 0,1,2: '))
    player1_val = list[player1_choice]
    print("Player1 Chose "+player1_val)

    random.shuffle(list)
    player2_choice = int(input('Enter Player2 Choice: 0,1,2: '))
    if(player2_choice >= 3):
        while(player2_choice >= 3):
            player2_choice = int(input('Enter Player2 Choice: 0,1,2: '))
    player2_val = list[player2_choice]
    print("Player2 Chose "+player2_val)
    if(player1_val == player2_val):
        print("its a tie!")
    else:
        if((player1_val == "rock") & (player2_val == "paper")):
            print("Player2 Won")
        elif((player1_val == "paper") & (player2_val == "scissors")):
            print("Player2 Won")
        elif((player1_val == "scissors") & (player2_val == "rock")):
            print("Player2 Won")
        else:
            print("Player 1 Won")
    exit_choice = input("Do you want to Exit? Y/N: ")
    if(exit_choice == "Y"):
        break
