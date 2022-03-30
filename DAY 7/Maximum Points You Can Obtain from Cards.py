class Solution:
    def maxScore(self, cp: List[int], k: int) -> int:
        if k==len(cp):
            return sum(cp)
        s=0
        e=len(cp)-k
        t=sum(cp[e:])
        ans=t
        while e<len(cp):
            t+=(cp[s]-cp[e])
            ans=max(ans,t)
            s+=1
            e+=1
        return ans
            
        