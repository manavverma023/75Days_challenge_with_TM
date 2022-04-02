class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=set(nums)
        ans=1
        while ans in nums:
            ans+=1
        return ans
        
        