class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)
        for R, h in enumerate(heights):
            L = R
            while stack and stack[-1][1] > h:
                L, h_i = stack.pop()
                maxArea = max(maxArea, (R - L)*h_i)
            stack.append((L, h))
        return maxArea