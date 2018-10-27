#!/usr/bin/env python3
# nrooks.py : Solve the N-Rooks problem!
#
# The N-Queens problem is: Given an empty NxN chessboard, place N queens on the board so that no queens
# can take any other, i.e. such that no two queens share the same row,column or are on the same diagonal
#
# Citations mentioned at the end of the code

import sys

# Count number of pieces in given row
def count_on_row(board, row):
    count=0
    # Iterate each node in every row
    #[2]
    for i in board[row]:
        if(i==1):
            count+=1
    return count

# Count number of pieces in given column
def count_on_col(board, col):
    count=0
    # Iterate over every column node of every row
    for x in ([a[col] for a in board]):
        if(x==1):
            count+=1
    return count

# Count total number of pieces on board
def count_pieces(board):
    count=0
    # Double for loop to check each node and update count
    for row in range(N):
        for col in range(N):
            if(board[row][col]==1):
                count+=1
    return count                

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    # Modifications done in display function to incorporate  unusable nodes and tag them as X with -1 as value
    #[4]
    if(problem_type=="nqueen"):
        return "\n".join([ " ".join([ "Q" if col==1 else "X" if col==-1 else "_" for col in row ]) for row in board])
    elif(problem_type=="nrook"):
        return "\n".join([ " ".join([ "R" if col==1 else "X" if col==-1 else "_" for col in row ]) for row in board])
    else:
        return "\n".join([ " ".join([ "K" if col==1 else "X" if col==-1 else "_" for col in row ]) for row in board])

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

# Successor function to place N rooks if given as the input argument.
# Sucessor function same as nrooks.py successors3()
def nrooks_successors(board):
    rook_number=count_pieces(board)
    if(rook_number<N and board!=[]):
        return [ add_piece(board, r, c) for c in range(0, rook_number+1) for r in range(0,N) if count_on_row(board,r)!=1 and count_on_col(board,c)!=1 and board[r][c]!=-1]
    else:
        return []

# Function to check if the queen is under attack with checking of diagonals
def check_position(board,r,c):
    if((count_on_row(board,r))==1 or (count_on_col(board,c)==1)):
        return True
    #Iterate from start of Board to check the presence of a queen with respect to current queen position 
    for board_row in range(0,N):
        for board_col in range(0,N):
            # The first condition checks if the diagonals perpendicular to current queen diagonal have any Queens already
            # The second condition checks for presence of queen above or below the current queen diagonal
            # [5]
            if((board_row+board_col==r+c) or (board_row-board_col==r-c)):
                if(board[board_row][board_col]==1):
                    return True
    return False

# Function to find and return successors of current board of N queens       
def nqueen_successors(board):
    # Accumaulate result state 
    result=[]
    rook_number=count_pieces(board)
    # Find all successors for current board in next column
    for c in range(0,rook_number+1):
        for r in range(0,N):
            # If any inner conditions is true the piece is not appended as a valid successor
            if(not(check_position(board,r,c)) and board[r][c]!=1 and board[r][c]!=-1):
                    result.append(add_piece(board,r,c))
    return result

# Function to check if the knight is under attack
def check_position_nknight(board,r,c):
    #Iterate from start of Board to check the presence of a queen with respect to current queen position 
    for board_row in range(0,N):
        for board_col in range(0,N):
            # The first condition checks if the diagonals perpendicular to current queen diagonal have any Queens already
            # The second condition checks for presence of queen above or below the current queen diagonal
            # [5]
            #print(board_row)
            #print(board_col)
            if(board[board_row][board_col]==1):
                if((int(r-board_row)**2)+(int(c-board_col)**2)==5):
                    return True
    return False
 
# Function to find and return successors of current board of N Knights 
def nknight_successors(board):
    # Accumaulate result state 
    result=[]
    #rook_number=count_pieces(board)
    # Find all successors for current board in next column
    for c in range(0,N):
        for r in range(0,N):
            # If any inner conditions is true the piece is not appended as a valid successor
            #print(check_position_nknight(board,r,c))
            if(not(check_position_nknight(board,r,c)) and board[r][c]!=1 and board[r][c]!=-1):
                #print(r)
                #print(c)
                #print("Rohit")
                result.append(add_piece(board,r,c))
    return result

# Check if board is a goal state without count_on_row or count_on_col function already checked in the successor
def is_goal(board):
    return count_pieces(board) == N 

# Solve for n-queen
def solve_dfs_nqueen(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in nqueen_successors( fringe.pop() ):
            if(count_pieces(s)==N):        
                if is_goal(s):
                    return(s)
            fringe.append(s)
    return False

# Solve for n-rooks
def solve_dfs_nrooks(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in nrooks_successors( fringe.pop() ):
            # Check only if N rooks are placed
            if(count_pieces(s)==N):        
                if is_goal(s):
                    return(s)
            fringe.append(s)
    return False

# Solution for n-knights
def solve_dfs_nknights(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in nknight_successors( fringe.pop() ):
            # Check only if N knights are placed
            if(count_pieces(s)==N):        
                if is_goal(s):
                    return(s)
            fringe.append(s)
    return False

# This is N, the size of the board. It is passed through command line arguments.
problem_type=str(sys.argv[1])    
N = int(sys.argv[2])

# Set initial board nodes to Zero
initial_board=[0]*N
for i in range(N):
    initial_board[i]=[0]*N
initial_board = [[0]*N for _ in range(N)]
#[3]

#Check if further arguments are provided for blocked positions
if(len(sys.argv)>3):
    blocked_places=int(sys.argv[3])
    for place in range(0,blocked_places):
        blocked_row=int(sys.argv[(place*2)+4])
        blocked_column=int(sys.argv[(place*2)+5])
        # Decide a blocked position with node filled as -1
        #[1]
        initial_board[blocked_row-1][blocked_column-1]=-1
        
print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")

# Call to different solve functions based on user input
if(problem_type=="nqueen"):
    solution = solve_dfs_nqueen(initial_board)
elif(problem_type=="nrook"):
    solution = solve_dfs_nrooks(initial_board)
else:
    solution = solve_dfs_nknights(initial_board)

print (printable_board(solution) if solution else "Sorry, no solution found. :(")

'''
[1] https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/ 
    Check solution states for N=4 for verification

[2] https://stackoverflow.com/questions/16548668/iterating-over-a-2-dimensional-python-list
    Iterating over a 2D array in python

[3] https://www.programiz.com/python-programming/matrix
    https://stackoverflow.com/questions/2739552/2d-list-has-weird-behavor-when-trying-to-modify-a-single-value
    Way of creating a 2D matrix with different references

[4] https://stackoverflow.com/questions/20888693/python-one-line-if-elif-else-statement/20888751
    if elif else statements on one line

[5] https://www.codesdope.com/blog/article/backtracking-explanation-and-n-queens-problem/
    Perpendicular Diagonal Check for current Queen Diagonal
'''

