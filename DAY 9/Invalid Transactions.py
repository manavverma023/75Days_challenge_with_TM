class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        nc=dict()
        ans=[]
        for i in transactions:
            t=i.split(",")
            if t[0] not in nc:
                nc[t[0]]=t[1:],
            else:
                nc[t[0]]+=t[1:],

        for i in transactions:
            t=i.split(",")
            if int(t[2])>1000:
                ans+=i,
                continue
            if t[0] in nc:
                for tt in nc[t[0]]:
                    if tt[-1]!=t[-1] and abs(int(tt[0])-int(t[1]))<=60:
                        ans+=i,
                        break
        return ans
                        
                
