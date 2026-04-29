class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        left_most = [-1 for i in range(len(heights))]
        right_most = [len(heights) for i in range(len(heights))]
        maxArea = 0
        s = []
        for i in range(len(heights)):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            if s:
                left_most[i] = s[-1]
            s.append(i)
        
        s = []
        for i in range(len(heights)-1, -1, -1):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            if s:
                right_most[i] = s[-1]
            s.append(i)
        
        print(left_most, right_most)
        for i in range(len(heights)):
            left_most[i] += 1
            right_most[i] -= 1
            maxArea = max(maxArea, heights[i] * (right_most[i] - left_most[i] + 1))
        return maxArea
