class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d={}
        ans=0
        for i in time:
            t=i%60
            if t==0:
                if t in d:
                    ans+=d[0]
            elif (60-t) in d:
                ans+=d[60-t]
            if t in d:
                d[t]+=1
            else:
                d[t]=1
        return ans