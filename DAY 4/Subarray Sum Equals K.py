class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        cs=0
        d={0:1}
        for i in nums:
            cs+=i
            dif=cs-k
            ans+=d.get(dif,0)
            d[cs]=1+d.get(cs,0)
        return ans