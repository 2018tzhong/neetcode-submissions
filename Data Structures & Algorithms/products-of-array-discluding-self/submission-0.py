class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fwd = [1 for i in range(len(nums))]
        bkwd = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            fwd[i] = nums[i-1] * fwd[i-1]

        for j in range(len(nums)-2, -1, -1):
            bkwd[j] = nums[j+1] * bkwd[j+1]
        
        result = [1 for i in range(len(nums))]
        for k in range(len(nums)):
            result[k] = fwd[k] * bkwd[k]
        
        return result
