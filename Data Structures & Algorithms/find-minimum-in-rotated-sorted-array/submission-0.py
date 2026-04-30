class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        def bs(low_el, high_el, nums):
            
            if high_el - low_el == 0:
                return high_el

            if high_el - low_el == 1:
                return low_el if nums[high_el] > nums[low_el] else high_el

            half = math.ceil(high_el - low_el) - 1
            if nums[low_el+half] > nums[high_el]:
                return bs(low_el + half, high_el, nums)
            else:
                return bs(low_el, low_el+half, nums)
        
        return nums[bs(0, len(nums)-1, nums)]