class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i,n in enumerate(nums):
            if i>0 and n==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                if n+nums[l]+nums[r]>0:
                    r-=1
                elif n+nums[l]+nums[r]<0:
                    l+=1
                else:
                    ans.append([n,nums[l],nums[r]])
                    l+=1
                    while nums[l-1]==nums[l] and l<r:
                        l+=1
        return ans
                            