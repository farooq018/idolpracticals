#Number of queens
print("Enter the number of queens")
N=int(input())

#chessboard
#NxN matrix with all element 0

board=[[0]*N for _ in range(N)]

def is_attack(i,j):
    #cheking if there is a queen in row or column
    for k in range(0,N):
        if board[i][k]==1 or board [k][j]==1:
            return True
    #checking diagonals
    for k in range(0,N):
        for i in range (0,N):
            if (k+1==i+j) or (k-1==i-j):
                if board[k][1]==1:
                    return True
    return False

def N_queen(n):
    #if n is 0, solution found
    if n==0:
       return True
    for i in range(0,N):
        for j in range(0,N):
            '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked or altready occupied'''
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j]=1
                #recursion
                #whether we can put the next queen with this arrangment or not
                if N_queen(n-1)==True:
                    return True
                board[i][j]=0
    return False

N_queen(N)
for i in board:
    print(i)