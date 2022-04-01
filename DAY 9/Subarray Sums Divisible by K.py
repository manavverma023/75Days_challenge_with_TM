class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d={0:1}
        cs=0
        ans=0
        for i in nums:
            cs+=i
            r=cs%k
            if r<0:
                cs+=k
            if r in d:
                ans+=d.get(r)
            d[r]=d.get(r,0)+1
        return ans