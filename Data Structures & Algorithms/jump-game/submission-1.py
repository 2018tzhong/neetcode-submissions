class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        start = len(nums) - 2
        curr_counter = 1
        while start > 0:
            if nums[start] >= curr_counter:
                curr_counter = 1
            else:
                curr_counter += 1
            start -= 1
        # for i in range(len(nums), -1, -1):
        return curr_counter <= nums[0] 
