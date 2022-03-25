class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=list(set(nums))
        m=0
        ans=0
        for i in range(len(n)):
            if nums.count(n[i])>m:
                m=nums.count(n[i])
                ans=n[i]
        return ans
        