
'''
Another problem brought up in CS374

N queens problem:
How many ways are there to place n non-attacking queens on an nxn chessboard?
Strategy: let board be an nxn chessboard. We will represent the position of a queen by a -1, and represent
a square that a queen can see with a positive number, which represents the number of queens that are looking at that square.
Define numQueens(row) that determines how many queens you can put on rows row->n, given that you've already placed queens on rows
1->row-1.

***Backtracking, not DP***
'''


n = (int)(input("Choose an n to calculate how many ways there are to put n queens on an nxn board: "))


board = []
for i in range(n):
    board.append([0] * n)




def printBoard():
    for row in board:
        print(row)
    print()

printBoard()

def placeQueen(row,col):
    if (board[row][col] > 0):
        return False #can't place a queen here because it's being attacked
    board[row][col] = -1
    for i in range(n):
        if (i != row):
            board[i][col] += 1
        if (i != col):
            board[row][i] += 1
        if (i != 0 and row-i >= 0 and col-i >= 0):
            board[row-i][col-i] += 1
        if (i != 0 and row+i < n and col-i >= 0):
            board[row+i][col-i] += 1
        if (i != 0 and row+i < n and col+i < n):
            board[row+i][col+i]  += 1
        if (i != 0 and row-i >= 0 and col+i < n):
            board[row-i][col+i] += 1
    return True#successfully placed queen

def removeQueen(row,col):
    if (board[row][col] >= 0):
        return False #no queen here
    board[row][col] = 0
    for i in range(n):
        if (i != row):
            board[i][col] -= 1
        if (i != col):
            board[row][i] -= 1
        if (i != 0 and row-i >= 0 and col-i >= 0):
            board[row-i][col-i] -= 1
        if (i != 0 and row+i < n and col-i >= 0):
            board[row+i][col-i] -= 1
        if (i != 0 and row+i < n and col+i < n):
            board[row+i][col+i]  -= 1
        if (i != 0 and row-i >= 0 and col+i < n):
            board[row-i][col+i] -= 1
    return True




def Nqueens(row):
    if (row == n):
        return 1#successfully placed n queens onto the board
    currsum = 0
    for i in range(n):
        if (placeQueen(row, i)):
            currsum += Nqueens(row+1)
            removeQueen(row,i)
    return currsum

print(Nqueens(0))