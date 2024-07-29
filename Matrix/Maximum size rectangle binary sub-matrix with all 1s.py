class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        maxArea = 0
        height = [0] * C
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == '1':
                    height[c] += 1
                else:
                    height[c] = 0
            area = self.largestRectangleArea(height)
            maxArea = max(maxArea, area)
        
        return maxArea
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea