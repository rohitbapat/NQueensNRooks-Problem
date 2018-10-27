# NQueensNRooks-Problem
Python program plotting NQueens and N Rooks and primitive approach for NKnights Problem

This program demonstrates search algorithms like BFS and DFS.
It basically finds for best possible solutions for a given set of inputs.
The set of inputs for the program are:
1] Type of problem NQueen, NRooks or Nknights.
2] The N value for N*N board.
3] The number of blocked positions.
4] A list of blocked places with row column identity.

Using fringe appends I have used iterations to find best possible and fastest solutions for a given board.

Solution of N Queens
For Queens problem we check the queens under attack when placed in same row,colum or diagonal.
I have checked this condition by checking row,column element for more than 1 ocurrences of Queens.
The diagonal check is done with respect to subtraction of coordinates of the queens under question.

Solution for N Rooks
For N Rooks we just need to check the same row same column ocurrences of the rooks.

Solution for N Knights
For N Knights the primitive solution is finding the Euclidean distance between the 2 Knights under question.
If it is exactly 5 then there are chances that the Knights can attack each other.

The blocked locations are denoted by 'X'. Hence the no of solutions may be limited. A solution might not exist
for a particualr board as well. For eg N Queen soltuion for 2*2 board does not exist.
Thus by selecting choice of problem type we can see the calculated board for the specific cases.