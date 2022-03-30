class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def dfs(i,c,total):
            if total==target:
                ans.append(c.copy())
                return 
            if i>=len(candidates) or total>target:
                return 
            
            c.append(candidates[i])
            dfs(i,c,total+candidates[i])
            c.pop()
            dfs(i+1,c,total)
        
        dfs(0,[],0)
        return ans