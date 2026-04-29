class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        results_0 = [nums[0], nums[1], nums[2]+nums[0]]
        results_1 = [nums[1], nums[2], nums[3]+nums[1]]

        for i in range(3, len(nums)):
            max_val = max(results_0[i-3], results_0[i-2])
            results_0.append(nums[i] + max_val)
        
        for i in range(4, len(nums)):
            max_val = max(results_1[-3], results_1[-2])
            results_1.append(nums[i] + max_val)
        
        print(results_0)
        print(results_1)


        possible_vals = [results_0[-2], results_0[-3], results_1[-1], results_1[-1]]
        return max(possible_vals)