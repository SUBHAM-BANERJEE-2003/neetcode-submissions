class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        ans = []
        for r in range(k-1, len(nums)):
            ans.append(max(nums[l : r + 1]))
            l += 1
        return ans