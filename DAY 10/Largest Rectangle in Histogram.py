class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans=0
        stack=[]
        
        for i,h in enumerate(heights):
            st=i
            while stack and stack[-1][1]>h:
                ind,height=stack.pop()
                ans=max(ans,height*(i-ind))
                st=ind
            stack.append((st,h))
        
        for i,h in stack:
            ans=max(ans,h*(len(heights)-i))
        return ans