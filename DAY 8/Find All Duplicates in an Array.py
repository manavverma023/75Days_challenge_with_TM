class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        s=set()
        for n in nums:
            if n in s:
                ans.append(n)
            s.add(n)
        return ans
        