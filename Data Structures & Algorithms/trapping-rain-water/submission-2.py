class Solution:
    def trap(self, height: List[int]) -> int:
        # pass through and compute the left max of each spot
        # pass through and compute the right max of each spot
        # then for each spot, we only need to take the min of those and diff with the spot

        left_max = [0 for i in range(len(height))]
        right_max = [0 for i in range(len(height))]

        curr_left_max = height[0]
        curr_right_max = height[-1]
        for i in range(1, len(height)):
            left_max[i] = max(curr_left_max, height[i-1])
            curr_left_max = max(curr_left_max, left_max[i])
        for j in range(len(height)-2, -1, -1):
            right_max[j] = max(curr_right_max, height[j+1])
            curr_right_max = max(curr_right_max, right_max[j])

        total_volume = 0
        for k in range(len(height)):
            total_volume += max(0, min(left_max[k], right_max[k]) - height[k])

        # print(left_max, right_max)
        return total_volume