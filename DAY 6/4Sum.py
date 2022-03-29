class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        temp=[]
        def cal(k,start,target):
            if k!=2:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    temp.append(nums[i])
                    cal(k-1,i+1,target-nums[i])
                    temp.pop()
                return 
                
            l=start
            r=len(nums)-1
            while(l<r):
                if nums[l]+nums[r]<target:
                    l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    ans.append(temp+[nums[l],nums[r]])
                    l+=1
                    while(l<r and nums[l]==nums[l-1]):
                        l+=1
        cal(4,0,target)
        return ans