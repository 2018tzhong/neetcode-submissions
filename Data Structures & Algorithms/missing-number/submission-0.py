class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = len(nums)
        expected_sum = (max_num + 1) * (len(nums)) / 2
        for num in nums:
            expected_sum -= num
        return int(expected_sum)