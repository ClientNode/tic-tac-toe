import math
import random
import time
import sys
import os

board = []
col = 3

for row in range(1,4):
    board.append(["*"] * col)

def get_board_pos(playerInput):
    board_positions_row = {1: 0, 2: 0, 3: 0,
                           4: 1, 5: 1, 6: 1,
                           7: 2, 8: 2, 9: 2}
    board_positions_col = {1: 0, 2: 1, 3: 2,
                           4: 0, 5: 1, 6: 2,
                           7: 0, 8: 1, 9: 2}
    return board_positions_row.get(playerInput), board_positions_col.get(playerInput)

def getPos(currentboard, pos):
    board_positions = {1: currentboard[0][0], 2: currentboard[0][1], 3: currentboard[0][2],
                       4: currentboard[1][0], 5: currentboard[1][1], 6: currentboard[1][2],
                       7: currentboard[2][0], 8: currentboard[2][1], 9: currentboard[2][2]}
    return board_positions.get(pos)

def place_marker(currentboard, pos):
    return True if getPos(currentboard, pos) == '*' else False

def check_win(currentboard, marker):
    return ((currentboard[0][0] == marker and currentboard[1][1] == marker and currentboard[2][2] == marker) or
            (currentboard[0][2] == marker and currentboard[1][1] == marker and currentboard[2][0] == marker) or
            (currentboard[0][0] == marker and currentboard[0][1] == marker and currentboard[0][2] == marker) or
            (currentboard[1][0] == marker and currentboard[1][1] == marker and currentboard[1][2] == marker) or
            (currentboard[2][0] == marker and currentboard[2][1] == marker and currentboard[2][2] == marker) or
            (currentboard[0][0] == marker and currentboard[1][0] == marker and currentboard[2][0] == marker) or
            (currentboard[0][1] == marker and currentboard[1][1] == marker and currentboard[2][1]== marker) or
            (currentboard[0][2] == marker and currentboard[1][2] == marker and currentboard[2][2] == marker))

def resetBoard(currentboard):
    for row in range(len(currentboard)):
        for col in range(len(currentboard[row])):
            currentboard[row][col] = '*'

def print_board(currentboard):
    for row in range(len(currentboard)):
        for col in range(len(currentboard[row])):
            print (currentboard[row][col],end=' ')
        print ()
    print(end='')
		
#Menu
counter = 0
menu = 0

while menu == 0:
    print ('Please Play In FullScreen!', file=sys.stderr)
    time.sleep(1)
    print ()
    print ()
    print ('|--------------------------------| 1|2|3         *|*|*        ')
    print ('|                                | -----         -----        ')
    print ('|                                | 4|5|6  ---->  *|*|*        ')
    print ('|                                | -----         -----        ')
    print ('|                                | 7|8|9         *|*|*        ')
    print ('|                                |      Directions:')
    print ('|       Tic - Tac - Toe          |      1) Get 3 in a row to win!')
    print ('|                                |      2) The second board is the one that will display.')
    print ('|                                |      3) Use the first board as a reference! ')
    print ('|                                |')
    print ('|                                |')
    print ('|--------------------------------|')
    print ()
    print ('A) =Singleplayer=')
    print ()
    print ('B) =Multiplayer=')
    print ()
    print ('C) =Exit=')
    print ()

    choose = input('Choose an option: ')

    #Exit Program
    if choose.lower() == 'c':
        print ()
        print ('Thanks for playing!')
        menu = 1

    #Multiplayer
    if choose.lower() == 'b':
        print ()
        print ('---Multiplayer---', file=sys.stderr)
        time.sleep(1)
        print ()

        #Picks random letters for players
        randompick = random.randint(0,1)
        
        if randompick == 0:
            player1 = 'X'
            player2 = 'O'
        else:
            player1 = 'O'
            player2 = 'X'

        print ('Player1 was randomly selected', player1, 'which leaves Player2 with', player2)
        print ()
        print ('1|2|3')
        print ('-----')
        print ('4|5|6')
        print ('-----')
        print ('7|8|9')
        print ()
        print ('The Real Board')
        print_board(board)

        while True:
            #PLAYER1
            player1input = int(input('Pick a Spot(Player1)[1-9]: '))            
            print ()

            if player1input > 9 or player1input < 1:
                print ('Invalid Spot')
                print ()
                continue

            if (place_marker(board, player1input)):
                player1_row, player1_col = get_board_pos(player1input)
                board[player1_row][player1_col] = player1
                print('\n------------------')
                print_board(board)
                counter = counter + 1
            else:
                print_board(board)
                print ('That Spot Is Taken')
                print ()
                continue
            time.sleep(1)
            print()

            #Check is Win
            if check_win(board, player1) is True:
                print("Player1 Wins! (Firework Sounds)")
                print()
                resetBoard(board)
                counter = 0
                break

            #Check Tie
            if counter > 4:
                print ('Tie Game!')
                print()
                resetBoard(board)
                counter = 0
                break

            #PLAYER 2
            while True:
                player2input = int(input('Pick a Spot(Player2)[1-9]: '))

                if player2input > 9 or player2input < 1:
                    print ('Invalid Spot')
                    print ()
                    continue
                print ()

                if (place_marker(board, player2input)):
                    player2_row, player2_col = get_board_pos(player2input)
                    board[player2_row][player2_col] = player2
                    print_board(board)
                    print('------------------\n')
                    break
                    #counter = counter + 1
                else:
                    print_board(board)
                    print ('That Spot Is Taken')
                    print ()
                    continue
                time.sleep(1)
                print()

            #Check if player2 Win           
            if check_win(board, player2) is True:
                print()
                print("Player2 Wins! (Firework Sounds)")
                print()
                resetBoard(board)
                counter = 0
                break
            
    #Singleplayer
    if choose.lower() == 'a':
        print ()
        print ('---Singleplayer---', file=sys.stderr)
        time.sleep(1)
        print ()

        #Randomly picks letter for computer
        randompick = random.randint(0,1)
        
        if randompick == 0:
            comp = 'X'
            player = 'O'
        else:
            comp = 'O'
            player = 'X'

        print ('The computer picked', comp, 'which leaves you with', player)
        print ()
        print ('1|2|3')
        print ('-----')
        print ('4|5|6')
        print ('-----')
        print ('7|8|9')
        print ()
        print ('The Real Board')
        print_board(board)

        while True:
            playerinput = int(input('\nRound {} \nPick a Spot[1-9]: '.format(counter + 1)))

            if playerinput > 9 or playerinput < 1:
                print ('Invalid Input')
                print ()
                continue

            if (place_marker(board, playerinput)):
                player_row, player_col = get_board_pos(playerinput)
                board[player_row][player_col] = player
                print('\n------------------')
                print_board(board)
                print()
                counter = counter + 1
            else:
                print ('That Spot Is Taken')
                print_board(board)
                continue
        
            #Check if player win
            if check_win(board, player) is True:
                print("You Win!")
                print()
                resetBoard(board)
                counter = 0
                break

            #Check Tie
            if counter > 4:
                print ('Tie Game!')
                print()
                resetBoard(board)
                counter = 0
                break
            
            while True:
                #Computer Picks Randomly
                computerpick = random.randint(1,9)

                if (place_marker(board, computerpick)):
                    comp_row, comp_col = get_board_pos(computerpick)
                    board[comp_row][comp_col] = comp
                    print_board(board)
                    print('------------------\n')
                    break
                else:
                    continue

            #Check if computer win        
            if check_win(board, comp) is True:
                print()
                print("HA, The Computer Beat You!")
                print()
                resetBoard(board)
                counter = 0
                break