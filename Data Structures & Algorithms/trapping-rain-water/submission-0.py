class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = [0] * n
        maxR = [0] * n
        lmsf = height[0]
        rmsf = height[n-1]
        trapwater = 0
        for i in range(1, n):
            maxL[i] = lmsf
            if height[i] > lmsf:
                lmsf = height[i]
        for i in range(n-1,-1,-1):
            maxR[i] = rmsf
            if height[i] > rmsf:
                rmsf = height[i]
        for i in range(n):
            currwater = min(maxL[i], maxR[i]) - height[i]
            if currwater > 0:
                trapwater += currwater
        print(*maxL," ",*maxR)
        return trapwater

            
