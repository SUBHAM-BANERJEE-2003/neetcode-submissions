class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        pre = 1
        for i in range(n):
            output[i] = pre
            pre *= nums[i]
        suf = 1
        for i in range(n-1, -1, -1):
            output[i] *= suf
            suf *= nums[i]
        return output
        