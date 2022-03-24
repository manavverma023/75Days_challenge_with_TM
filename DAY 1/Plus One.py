class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s="".join(map(str,digits))
        #print(type(s))
        s=int(s)
        s=s+1
        s=list(str(s))
        for i in s:
            i=int(i)
        return s
        