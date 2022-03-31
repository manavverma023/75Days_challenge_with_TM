class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans=0
        d=dict(Counter(nums))
        if k==0:
            for i in d.values():
                if i>1:
                    ans+=1
        else:
            for i in d.keys():
                if d.get(i+k,0)!=0:
                    ans+=1
        return ans