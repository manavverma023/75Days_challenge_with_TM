class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row,col=len(board),len(board[0])
        t=set()
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=row or c>=col or board[r][c]!=word[i] or (r,c) in t:
                return False
            t.add((r,c))
            ans=(dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            t.remove((r,c))
            return ans
        for i in range(row):
            for j in range(col):
                if dfs(i,j,0):
                    return True
        return False