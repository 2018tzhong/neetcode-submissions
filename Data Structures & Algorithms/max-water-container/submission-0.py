class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        max_vol = (p2-p1) * min(heights[p2], heights[p1])
        while p2 > p1:
            max_vol = max(max_vol, (p2-p1) * min(heights[p2], heights[p1]))
            if heights[p2] < heights[p1]:
                p2 -= 1
            else:
                p1 += 1

        return max_vol
