class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        l=0
        h=0
        intervals.sort()
        for n,i in enumerate(intervals):
            if n==0:
                l=i[0]
                h=i[1]
                #print("if",l," ",h)
            elif i[0]>h:
                ans.append([l,h])
                l=i[0]
                h=i[1]
                #print(l," ",h)
            elif i[0]>=l or i[1]<=h:
                l=min(l,i[0])
                h=max(h,i[1])
                #print("elif", l," ",h)
            
        if [l,h] not in ans:
            ans.append([l,h])
        return ans