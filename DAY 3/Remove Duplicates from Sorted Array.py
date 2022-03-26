class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set(nums)
        li=list(s)
        ans=len(li)
        nums.clear()
        nums.extend(li)
        nums.sort()
        return ans
        
            
        