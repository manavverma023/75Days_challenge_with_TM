class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        mh=0
        mw=0
        ph=0
        hc.append(h)
        vc.append(w)
        hc.sort()
        vc.sort()
        for i in hc:
            mh=max(i-ph,mh)
            ph=i
        pw=0
        for i in vc:
            mw=max(i-pw,mw)
            pw=i
        return (mh*mw)%1000000007