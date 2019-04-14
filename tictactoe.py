import math
import random
import time
import sys

board = []
col = 3

for row in range(1,4):
    board.append(["*"] * col)

def print_board(playboard):
    for row in range(len(playboard)):
        for col in range(len(playboard[row])):
            print (playboard[row][col],end=' ')
        print ()
        
#*******Prints the board*********
'''
print_board(board)
print ()     
'''

def check_comp_win(board):
    #Diagonal Win
    if board[0][0] == comp and board[1][1] == comp and board[2][2] == comp:
        print ()
        print ('HA, The Computer Beat You!')
        print ()
        return True

    elif board[0][2] == comp and board[1][1] == comp and board[2][0] == comp:
        print ()
        print ('HA, The Computer Beat You!')
        print ()
        return True

    #Horizontial Win    
    elif board[0][0] == comp and board[0][1] == comp and board[0][2] == comp:
        print ()
        print ('HA, The Computer Beat You!')
        print ()
        return True

    elif board[1][0] == comp and board[1][1] == comp and board[1][2] == comp:
        print ()
        print ('HA, The Computer Beat You!')
        print ()
        return True

    elif board[2][0] == comp and board[2][1] == comp and board[2][2] == comp:
        print ()
        print ('HA, The Computer Beat You!')
        print ()
        return True

    #Vertical Win
    elif board[0][0] == comp and board[1][0] == comp and board[2][0] == comp:
        print ()
        print ('HA, The Computer Beat You!')
        print ()
        return True

    elif board[0][1] == comp and board[1][1] == comp and board[2][1] == comp:
        print ()
        print ('HA, The Computer Beat You!')
        print ()
        return True

    elif board[0][2] == comp and board[1][2] == comp and board[2][2] == comp:
        print ()
        print ('HA, The Computer Beat You!')
        print ()
        return True

def check_player_win(board):
    #Diagonal Win
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print ()
        print ('You Win!')
        print ()
        return True

    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print ()
        print ('You Win!')
        print ()
        return True

    #Horizontial Win    
    elif board[0][0] == player and board[0][1] == player and board[0][2] == player:
        print ()
        print ('You Win!')
        print ()
        return True

    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        print ()
        print ('You Win')
        print ()
        return True

    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        print ()
        print ('You Win!')
        print ()
        return True

    #Vertical Win
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        print ()
        print ('You Win!')
        print ()
        return True

    elif board[0][1] == player and board[1][1] == player and board[2][1]== player:
        print ()
        print ('You Win!')
        print ()
        return True

    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        print ()
        print ('You Win!')
        print ()
        return True

def multi_player1_win(board):
    #Diagonal Win
    if board[0][0] == player1 and board[1][1] == player1 and board[2][2] == player1:
        print ()
        print ('Player1 Wins! (Firework Sounds)')
        print ()
        return True
        
    elif board[0][2] == player1 and board[1][1] == player1 and board[2][0] == player1:
        print ()
        print ('Player1 Wins! (Firework Sounds)')
        print ()
        return True

    #Horizontial Win    
    elif board[0][0] == player1 and board[0][1] == player1 and board[0][2] == player1:
        print ()
        print ('Player1 Wins! (Firework Sounds)')
        print ()
        return True

    elif board[1][0] == player1 and board[1][1] == player1 and board[1][2] == player1:
        print ()
        print ('Player1 Wins! (Firework Sounds)')
        print ()
        return True

    elif board[2][0] == player1 and board[2][1] == player1 and board[2][2] == player1:
        print ()
        print ('Player1 Wins! (Firework Sounds)')
        print ()
        return

    #Vertical Win
    elif board[0][0] == player1 and board[1][0] == player1 and board[2][0] == player1:
        print ()
        print ('Player1 Wins! (Firework Sounds)')
        print ()
        return True

    elif board[0][1] == player1 and board[1][1] == player1 and board[2][1]== player1:
        print ()
        print ('Player1 Wins! (Firework Sounds)')
        print ()
        return True

    elif board[0][2] == player1 and board[1][2] == player1 and board[2][2] == player1:
        print ()
        print ('Player1 Wins! (Firework Sounds)')
        print ()
        return True
    
def multi_player2_win(board):
    #Diagonal Win
    if board[0][0] == player2 and board[1][1] == player2 and board[2][2] == player2:
        print ()
        print ('Player2 Wins! (Firework Sounds)')
        print ()
        return True

    elif board[0][2] == player2 and board[1][1] == player2 and board[2][0] == player2:
        print ()
        print ('Player2 Wins! (Firework Sounds)')
        print ()
        return True

    #Horizontial Win    
    elif board[0][0] == player2 and board[0][1] == player2 and board[0][2] == player2:
        print ()
        print ('Player2 Wins! (Firework Sounds)')
        print ()
        return True

    elif board[1][0] == player2 and board[1][1] == player2 and board[1][2] == player2:
        print ()
        print ('Player2 Wins! (Firework Sounds)')
        print ()
        return True

    elif board[2][0] == player2 and board[2][1] == player2 and board[2][2] == player2:
        print ()
        print ('Player2 Wins! (Firework Sounds)')
        print ()
        return True

    #Vertical Win
    elif board[0][0] == player2 and board[1][0] == player2 and board[2][0] == player2:
        print ()
        print ('Player2 Wins! (Firework Sounds)')
        print ()
        return True

    elif board[0][1] == player2 and board[1][1] == player2 and board[2][1]== player2:
        print ()
        print ('Player2 Wins! (Firework Sounds)')
        print ()
        return True

    elif board[0][2] == player2 and board[1][2] == player2 and board[2][2] == player2:
        print ()
        print ('Player2 Wins! (Firework Sounds)')
        print ()
        return True
		
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
    if choose == 'C' or choose == 'c':
        print ()
        print ('Do you really want to exit?')
        leave = input('[Y/N]: ')
        print ()
        if leave == 'Y' or leave == 'y':
            print ('Thanks for playing!')
            menu = 1
            
        else:
            menu = 0
            print ()

    #Multiplayer
    if choose == 'B' or choose == 'b':
        print ()
        print ('---Multiplayer---', file=sys.stderr)
        time.sleep(1)
        print ()

        #Picks random letters for players
        randompick = random.randint(0,1)
        player1 = randompick
        player2 = randompick
        
        if randompick == 0:
            player1 = 'X'
            player2 = 'O'

        elif randompick == 1:
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
        print ()

        while True:
            #PLAYER1
            player1input = int(input('Pick a Spot(Player1)[1-9]: '))            
            print ()

            if player1input > 9 or player1input < 1:
                print ('Invalid Spot')
                print ()
                continue
            
            if player1input == 1:
                if board[0][0] == 'O' or board[0][0] == 'X':
                    print ('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[0][0] = player1
                    counter = counter + 1
                print_board(board)
                time.sleep(1)
                print ()

            elif player1input == 2:
                if board[0][1] == 'O' or board[0][1] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[0][1] = player1
                    counter = counter + 1
                print_board(board)
                time.sleep(1)
                print ()

            elif player1input == 3:
                if board[0][2] == 'O' or board[0][2] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[0][2] = player1
                    counter = counter + 1
                print_board(board)
                time.sleep(1)
                print ()

            elif player1input == 4:
                if board[1][0] == 'O' or board[1][0] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[1][0] = player1
                    counter = counter + 1
                print_board(board)
                time.sleep(1)
                print ()

            elif player1input == 5:
                if board[1][1] == 'O' or board[1][1] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[1][1] = player1
                    counter = counter + 1
                print_board(board)
                time.sleep(1)
                print ()

            elif player1input == 6:
                if board[1][2] == 'O' or board[1][2] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[1][2] = player1
                    counter = counter + 1
                print_board(board)
                time.sleep(1)
                print ()

            elif player1input == 7:
                if board[2][0] == 'O' or board[2][0] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[2][0] = player1
                    counter = counter + 1
                print_board(board)
                time.sleep(1)
                print ()

            elif player1input == 8:
                if board[2][1] == 'O' or board[2][1] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[2][1] = player1
                    counter = counter + 1
                print_board(board)
                time.sleep(1)
                print ()

                
            elif player1input == 9:
                if board[2][2] == 'O' or board[2][2] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[2][2] = player1
                    counter = counter + 1
                print_board(board)
                time.sleep(1)
                print ()

            #Check is Win
            if multi_player1_win(board) is True:
                board[0][0] = '*'
                board[0][1] = '*'
                board[0][2] = '*'
                board[1][0] = '*'
                board[1][1] = '*'
                board[1][2] = '*'
                board[2][0] = '*'
                board[2][1] = '*'
                board[2][2] = '*'
                counter = 0
                break

            #Check Tie
            if counter > 4:
                print ('Tie Game!')
                board[0][0] = '*'
                board[0][1] = '*'
                board[0][2] = '*'
                board[1][0] = '*'
                board[1][1] = '*'
                board[1][2] = '*'
                board[2][0] = '*'
                board[2][1] = '*'
                board[2][2] = '*'
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

                if player2input == 1:
                    if board[0][0] == 'O' or board[0][0] == 'X':
                        print ('That Spot Is Taken')
                        print ()
                        continue
                        
                    else:
                        board[0][0] = player2
                        print_board(board)
                        print ()
                        break
                    print ()

                elif player2input == 2:
                    if board[0][1] == 'O' or board[0][1] == 'X':
                        print('That Spot Is Taken')
                        print ()
                        continue
                        
                    else:
                        board[0][1] = player2
                        print_board(board)
                        print ()
                        break
                    print ()

                elif player2input == 3:
                    if board[0][2] == 'O' or board[0][2] == 'X':
                        print('That Spot Is Taken')
                        print ()
                        continue
                        
                    else:
                        board[0][2] = player2
                        print_board(board)
                        print ()
                        break
                    print ()

                elif player2input == 4:
                    if board[1][0] == 'O' or board[1][0] == 'X':
                        print('That Spot Is Taken')
                        print ()
                        continue
                        
                    else:
                        board[1][0] = player2
                        print_board(board)
                        print ()
                        break
                    print ()

                elif player2input == 5:
                    if board[1][1] == 'O' or board[1][1] == 'X':
                        print('That Spot Is Taken')
                        print ()
                        continue
                        
                    else:
                        board[1][1] = player2
                        print_board(board)
                        print ()
                        break
                    print ()

                elif player2input == 6:
                    if board[1][2] == 'O' or board[1][2] == 'X':
                        print('That Spot Is Taken')
                        print ()
                        continue
                        
                    else:
                        board[1][2] = player2
                        print_board(board)
                        print ()
                        break
                    print ()

                elif player2input == 7:
                    if board[2][0] == 'O' or board[2][0] == 'X':
                        print('That Spot Is Taken')
                        print ()
                        continue
                        
                    else:
                        board[2][0] = player2
                        print_board(board)
                        print ()
                        break
                    print ()

                elif player2input == 8:
                    if board[2][1] == 'O' or board[2][1] == 'X':
                        print('That Spot Is Taken')
                        print ()
                        continue
                        
                    else:
                        board[2][1] = player2
                        print_board(board)
                        print ()
                        break
                    print ()

                        
                elif player2input == 9:
                    if board[2][2] == 'O' or board[2][2] == 'X':
                        print('That Spot Is Taken')
                        print ()
                        continue
                        
                    else:
                        board[2][2] = player2
                        print_board(board)
                        print ()
                        break
                    print ()
            #Check if player2 Win           
            if multi_player2_win(board) is True:
                board[0][0] = '*'
                board[0][1] = '*'
                board[0][2] = '*'
                board[1][0] = '*'
                board[1][1] = '*'
                board[1][2] = '*'
                board[2][0] = '*'
                board[2][1] = '*'
                board[2][2] = '*'
                counter = 0
                break
            
    #Singleplayer
    if choose == 'A' or choose == 'a':
        print ()
        print ('---Singleplayer---', file=sys.stderr)
        time.sleep(1)
        print ()

        #Randomly picks letter for computer
        randompick = random.randint(0,1)
        
        if randompick == 0:
            comp = 'X'
            player = 'O'

        elif randompick == 1:
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
        print ()

        while True:
            playerinput = int(input('Pick a Spot[1-9]: '))
            print ()

            if playerinput > 9 or playerinput < 1:
                print ('Invalid Input')
                print ()
                continue

            if playerinput == 1:
                if board[0][0] == 'O' or board[0][0] == 'X':
                    print ('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[0][0] = player
                    print_board(board)
                    counter = counter + 1
                time.sleep(1)
                print ()

            elif playerinput == 2:
                if board[0][1] == 'O' or board[0][1] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[0][1] = player
                    print_board(board)
                    counter = counter + 1
                time.sleep(1)
                print ()

            elif playerinput == 3:
                if board[0][2] == 'O' or board[0][2] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[0][2] = player
                    print_board(board)
                    counter = counter + 1
                time.sleep(1)
                print ()

            elif playerinput == 4:
                if board[1][0] == 'O' or board[1][0] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[1][0] = player
                    print_board(board)
                    counter = counter + 1
                time.sleep(1)
                print ()

            elif playerinput == 5:
                if board[1][1] == 'O' or board[1][1] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[1][1] = player
                    print_board(board)
                    counter = counter + 1
                time.sleep(1)
                print ()

            elif playerinput == 6:
                if board[1][2] == 'O' or board[1][2] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[1][2] = player
                    print_board(board)
                    counter = counter + 1
                time.sleep(1)
                print ()

            elif playerinput == 7:
                if board[2][0] == 'O' or board[2][0] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[2][0] = player
                    print_board(board)
                    counter = counter + 1
                time.sleep(1)
                print ()

            elif playerinput == 8:
                if board[2][1] == 'O' or board[2][1] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[2][1] = player
                    print_board(board)
                    counter = counter + 1
                time.sleep(1)
                print ()

                
            elif playerinput == 9:
                if board[2][2] == 'O' or board[2][2] == 'X':
                    print('That Spot Is Taken')
                    print ()
                    continue
                
                else:
                    board[2][2] = player
                    print_board(board)
                    counter = counter + 1
                time.sleep(1)
                print ()

            #Check if player win
            if check_player_win(board) is True:
                board[0][0] = '*'
                board[0][1] = '*'
                board[0][2] = '*'
                board[1][0] = '*'
                board[1][1] = '*'
                board[1][2] = '*'
                board[2][0] = '*'
                board[2][1] = '*'
                board[2][2] = '*'
                counter = 0
                break

            #Check Tie
            if counter > 4:
                print ('Tie Game!')
                board[0][0] = '*'
                board[0][1] = '*'
                board[0][2] = '*'
                board[1][0] = '*'
                board[1][1] = '*'
                board[1][2] = '*'
                board[2][0] = '*'
                board[2][1] = '*'
                board[2][2] = '*'
                counter = 0
                break
            
            while True:
                #Computer Picks Randomly
                computerpick = random.randint(1,9)

                if counter > 4:
                    print ('Tie Game!')
                    board[0][0] = '*'
                    board[0][1] = '*'
                    board[0][2] = '*'
                    board[1][0] = '*'
                    board[1][1] = '*'
                    board[1][2] = '*'
                    board[2][0] = '*'
                    board[2][1] = '*'
                    board[2][2] = '*'
                    counter = 0
                    break
           
                if computerpick == 1:
                    if board[0][0] == 'O' or board[0][0] == 'X':
                        continue
                    
                    else:
                        board[0][0] = comp
                        print_board(board)
                        break
                    time.sleep(1)
                    print ()
                    
                elif computerpick == 2:
                    if board[0][1] == 'O' or board[0][1] == 'X':
                        continue
                    
                    else:
                        board[0][1] = comp
                        print_board(board)
                        break
                    time.sleep(1)
                    print ()

                elif computerpick == 3:
                    if board[0][2] == 'O' or board[0][2] == 'X':
                        continue
                    
                    else:
                        board[0][2] = comp
                        print_board(board)
                        break
                    time.sleep(1)
                    print ()

                elif computerpick == 4:
                    if board[1][0] == 'O' or board[1][0] == 'X':
                        continue

                    else:
                        board[1][0] = comp
                        print_board(board)
                        break
                    time.sleep(1)
                    print ()

                elif computerpick == 5:
                    if board[1][1] == 'O' or board[1][1] == 'X':
                        continue

                    else:
                        board[1][1] = comp
                        print_board(board)
                        break
                    time.sleep(1)
                    print ()

                elif computerpick == 6:
                    if board[1][2] == 'O' or board[1][2] == 'X':
                        continue

                    else:
                        board[1][2] = comp
                        print_board(board)
                        break
                    time.sleep(1)
                    print ()

                elif computerpick == 7:
                    if board[2][0] == 'O' or board[2][0] == 'X':
                        continue

                    else:
                        board[2][0] = comp
                        print_board(board)
                        break
                    time.sleep(1)
                    print ()

                elif computerpick == 8:
                    if board[2][1] == 'O' or board[2][1] == 'X':
                        continue

                    else:
                        board[2][1] = comp
                        print_board(board)
                        break
                    time.sleep(1)
                    print ()
                
                elif computerpick == 9:
                    if board[2][2] == 'O' or board[2][2] == 'X':
                        continue

                    else:
                        board[2][2] = comp
                        print_board(board)
                        break
                    time.sleep(1)
                    print ()

            #Check if computer win        
            if check_comp_win(board) is True:
                board[0][0] = '*'
                board[0][1] = '*'
                board[0][2] = '*'
                board[1][0] = '*'
                board[1][1] = '*'
                board[1][2] = '*'
                board[2][0] = '*'
                board[2][1] = '*'
                board[2][2] = '*'
                counter = 0
                break
