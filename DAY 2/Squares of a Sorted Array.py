class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            ans.append(i**2)
        ans.sort()
        return ans