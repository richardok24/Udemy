from IPython.display import clear_output
import random

def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9]+'\n'+'-----'+'\n'+board[4]+'|'+board[5]+'|'+board[6]+'\n'+'-----'+'\n'+board[1]+'|'+board[2]+'|'+board[3])

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Please pick a marker 'X' or 'O': ").upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return (board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) or (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark) or (board[1]==board[5]==board[9]==mark) or (board[3]==board[5]==board[7]==mark)

def choose_first():
    randomNumber = random.randint(1,10)
    if randomNumber <= 5:
        return 'Player 1 goes first'
    else:
        return 'Player 2 goes first'
    
def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' not in board[1:]

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Please enter the position (1-9) of your next move: '))
    return position

def replay():
    selection = ''
    while selection != 'yes' and selection != 'no':
        selection = input('Would you like to play again? (Type in yes or no)').lower()
    if selection == 'yes':
        return True
    else:
        return False
    
print('Welcome to Tic Tac Toe!')

#while True:
while True:
    # Set the game up here
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? (yes or no?) ').lower()
    if play_game == 'yes':
        game_on = True
    else:
        game_on = False

    #while game_on:
    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            
            # Show the board
            display_board(the_board)
            
            # Choose a position
            position = player_choice(the_board)
            
            # Place the marker on the position
            place_marker(the_board, player1_marker, position)
            
            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!!!')
                game_on = False
            
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!!!')
                    game_on = False
                else:
                    turn = 'Player 2'
        
        # Player2's turn.
        else:
            # Show the board
            display_board(the_board)
            
            # Choose a position
            position = player_choice(the_board)
            
            # Place the marker on the position
            place_marker(the_board, player2_marker, position)
            
            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 1 has won!!!')
                game_on = False
            
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game!!!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
