class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        cp=0
        ans=0
        while(r<len(prices)):
            cp=prices[r]-prices[l]
            if prices[l]<prices[r]:
                ans=max(ans,cp)
            else:
                l=r
            r+=1
        return ans
        