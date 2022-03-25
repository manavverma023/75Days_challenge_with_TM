class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t=sum(nums)
        cs=0
        for i in range(len(nums)):
            if i!=0:
                cs+=nums[i-1]
                t-=nums[i]
            else:
                t-=nums[i]
            if cs==t:
                return i
        return -1