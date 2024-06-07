#!/usr/bin/env python
# coding: utf-8

# # Project Description

# During my ECE 15 Engineering Computation course, I learned the C programming language. One of our programming assignments was to write a Connect-4 game. Due to my limited knowledge of C, the complexity of the instructions, and the intricacies of the language, I ended up writing 120 lines of code and struggled with numerous bugs. Now, as I am learning Python in my COGS 18 course, I often wonder how much easier it would be to write the game in Python. For my final project, I decided to rewrite the Connect-4 game in Python, combining the logic I developed in ECE 15 with the new skills I've gained in COGS 18.
# 
# I used NumPy to create the Connect-4 board, initializing all positions to 0. I then wrote a function, 'valid_location', to check if the top row of a column is filled. The 'piece_play' and 'drop_piece' functions simulate dropping a Connect-4 piece ('1' and '2') as in the real game. The most challenging part was writing the 'winning' condition logic. I used nested loops to check for horizontal, vertical, and diagonal wins.
# 
# Next, I created the game loop, where the board is printed after each move, and players input the column they want to drop their piece into. I also implemented input validation to ensure entries are within range and are not strings. The game runs in a 'while true' loop, alternating turns between players until one wins, which is determined by the 'winning' function. If the board fills up without a winner, the game ends in a draw.
# 
# I do get the approval of the professor by doing this as a project, I have attached the approval message and also my old ECE code with PA intructions in another text file called 'references'.  
# 
# I believe this project can demonstrates my continuous improvement in coding and my eagerness to learn new things. I hope this project brings joy to those who play it, including both my ECE 15 friends and COGS 18 friends.

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[1]:


#from my_module.functions import ...
#from my_module.classes import ...
import numpy as np


# In[2]:


#import numpy as np

def make_board():
    return np.zeros((6, 7))

def valid_location(board, col):
    return board[5][col] == 0
    #print(is_valid_location)
    
def piece_play(board, row, col, piece):
    board[row][col] = piece

def drop_piece(board, col):
    for r in range(6):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning(board, piece):

    for c in range(4):
        for r in range(6):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True


    for c in range(7):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True


    for c in range(4):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True


    for c in range(4):
        for r in range(3, 6):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def game_play():
    board = make_board()
    print_board(board)
    turn = 0

    while True:
       
        if turn % 2 == 0 or turn == 0:
            a = input("Player 1, make your selection (1-7):")
            try: 
                col = int(a)
            except: 
                print("Invalid move. Try again.")
                continue
            col -= 1
            
            if col < 0 or col > 6:
                print("Invalid move. Try again.")
                continue
    
            if valid_location(board, col):
                row = drop_piece(board, col)
                piece_play(board, row, col, 1)

                if winning(board, 1):
                    print("Player 1 wins!")
                    break
            else:
                print("Invalid move. Try again.")
                continue


        else:
            b = input("Player 2, make your selection (1-7):")
            try: 
                col = int(b)
            except: 
                print("Invalid move. Try again.")
                continue
            col -= 1
            
            if col < 0 or col > 6:
                print("Invalid move. Try again.")
                continue
                
            if valid_location(board, col):
                row = drop_piece(board, col)
                piece_play(board, row, col, 2)

                if winning(board, 2):
                    print("Player 2 wins!")
                    break
            else:
                print("Invalid move. Try again.")
                continue

        print_board(board)
        turn += 1
        if turn == 42:
            print("Drawn Game!")
            break
    print_board(board)


# In[ ]:


game_play()


# #### Extra Credit (*optional*)
# I have never learned python in my life but I have some background of coding in programm language C by taking ECE 15 course. My project went pretty smooth since I already have logic in my mind the only hard part is to put them down as codes. I challenged myself by using NumPy to help create my project which I find hard to understand and avoid to use. 
# 
