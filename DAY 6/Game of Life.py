class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,col=len(board),len(board[0])
        def co(r,c):
            n=0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if ((i==r and j==c) or i<0 or j<0 or i==row or j==col):
                        continue
                    if board[i][j] in [1,3]:
                        n+=1
            return n
        for i in range(row):
            for j in range(col):
                n=co(i,j)
                if board[i][j]:
                    if n in [2,3]:
                        board[i][j]=3
                elif n==3:
                    board[i][j]=2
        
        for i in range(row):
            for j in range(col):
                if board[i][j] in [2,3]:
                    board[i][j]=1
                elif board[i][j]==1:
                    board[i][j]=0  