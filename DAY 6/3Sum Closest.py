class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=sum(nums[:3])
        for i in range(len(nums)-2):
            s=i+1
            e=len(nums)-1
            while(s<e):
                ts=nums[i]+nums[s]+nums[e]
                if abs(ts-target)<abs(ans-target):
                    ans=ts
                if ts<target:
                    s+=1
                else:
                    e-=1
        return ans