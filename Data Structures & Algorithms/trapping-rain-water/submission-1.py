class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        L = 0
        R = n - 1
        lmax = height[L]
        rmax = height[R]
        trapwater = 0
        while L < R:
            if lmax < rmax:
                L += 1
                lmax = max(height[L], lmax)
                trapwater += lmax - height[L]
            else:
                R -= 1
                rmax = max(height[R], rmax)
                trapwater += rmax - height[R]
        return trapwater

            
