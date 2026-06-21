import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles) 
        ans = R
        while L <= R:
            mid = L + (R - L) // 2
            h_calc = sum(math.ceil(pile / mid) for pile in piles)
            if h_calc <= h:
                ans = mid
                R = mid - 1
            else:
                L = mid + 1
        return ans