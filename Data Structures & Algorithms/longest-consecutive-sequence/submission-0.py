class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for n in nums:
            if n-1 not in nums:
                currlen, currnum = 0, n
                while currnum in s:
                    currlen += 1
                    currnum += 1
                ans = max(ans, currlen)
        return ans
