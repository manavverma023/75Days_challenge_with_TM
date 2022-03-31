class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        v=set()
        def dfs(r,c):
            if r<0 or r==row or c<0 or c==col or grid[r][c]==0 or (r,c) in v:
                return 0
            v.add((r,c))
            return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
        ans=0
        for i in range(row):
            for j in range(col):
                ans=max(ans,dfs(i,j))
        return ans