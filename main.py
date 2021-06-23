# -----Global Variable -----
# Game Board
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-"]

# If game is still running
game_running = True

# Who Won?
winner = None

# Whose turn is it?
current_player = "X"
#--------Functions----------
# Play a game of tic tac toe
def play_game():

  # Display initial board
  display_board()

  while game_running:

    # vhandle a single turn of an arbitrary player
    turn(current_player)
    
    # check if game has ended 
    check_if_game_over()
    # Flip to the other player
    flip_player()
  
  # Game ended, print winner
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")

# Display board
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])
  print("\n")

# Handle a single turn of an arbitrary player
def turn(player):

  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Put the game piece on the board
  board[position] = player

  # Show the game board
  display_board()

def check_if_game_over():
  check_for_win()
  check_if_tie()

#Check to see if someone has won
def check_for_win():
  # Set up global variables
  global winner
  #check rows
  row_win = check_rows()
  #check coloumns
  col_win = check_col()
  #check diagonals
  diagonal_win = check_diagonals()
  if row_win:
    winner = row_win
  elif col_win:
    winner = col_win
  elif diagonal_win:
    winner = diagonal_win
  else:
    winner = None

def check_rows():
  # Set up global variable 
  global game_running
  # check if any of the rows have the same value and is not empty.
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  #If any row has a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_running = False
  # Return the winner (X or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  # Else return None if there was no winner
  else:
    return None

def check_col():
  global game_running
  # check if any of the columns have the same value and is not empty.
  col_1 = board[0] == board[3] == board[6] != "-"
  col_2 = board[1] == board[4] == board[7] != "-"
  col_3 = board[2] == board[5] == board[8] != "-"
  #If any column has a match, flag that there is a win
  if col_1 or col_2 or col_3:
    game_running = False
  # Return the winner (X or O)
  if col_1:
    return board[0]
  elif col_2:
    return board[1]
  elif col_3:
    return board[2]
  # Else return None if there was no winner
  else:
    return None

def check_diagonals():
  global game_running
  # check if any of the diagonal have the same value and is not empty.
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  #If any diagonal has a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_running = False
  # Return the winner (X or O)
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  # Return None if there was no winner 
  else:
    return None
  

def check_if_tie():
  # Global Variable
  global game_running
  # If board is full
  if "-" not in board:
    game_running = False
    return True
  # Else there is no tie
  else:
    return False
   
def flip_player():
  # Global Variable
  global current_player
  # If the current player was X, change it to O
  if current_player == "X":
    current_player = "O"
  # If the current player was O, change it to X
  elif current_player == "O":
    current_player = "X"
  return

#--------Execution-------
# Play a game of tic tac toe
play_game()
