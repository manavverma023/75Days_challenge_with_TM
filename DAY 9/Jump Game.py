class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans=0
        for i in range(len(nums)):
            if i>ans:
                return False
            ans=max(ans,i+nums[i])
        return True
            
        