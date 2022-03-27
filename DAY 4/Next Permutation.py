class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=l=len(nums)-1
        while i>0:
            if nums[i]>nums[i-1]:
                tmp=0
                for j in range(l,i-1,-1):
                    if nums[j]>nums[i-1]:
                        tmp=j
                        break
                nums[i-1],nums[tmp]=nums[tmp],nums[i-1]
                for j in range(i,1+i+(l-i)//2):
                    nums[j],nums[l+i-j]=nums[l+i-j],nums[j]
                break
            i-=1
        if i==0:
            nums.reverse()