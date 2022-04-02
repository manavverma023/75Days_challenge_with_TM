class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=[-inf]*3
        s=[0]*3
        
        for i in prices:
            for j in range(1,3):
                b[j]=max(b[j],s[j-1]-i)
                s[j]=max(b[j]+i,s[j])
        return s[2]