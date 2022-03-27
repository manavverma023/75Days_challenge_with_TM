class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        l=0
        r=len(height)-1
        while(l<r):
            area=(r-l)*min(height[r],height[l])
            ans=max(area,ans)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans