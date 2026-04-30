import pdb

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # use a bs to find the minimum element, use that to cut, 
        # then do binary search on each one to find the 
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

        min_idx = bs(0, len(nums)-1, nums)
        
        def bs_exact(low_el, high_el, nums, target):

            if high_el < low_el:
                return low_el
            if high_el - low_el == 0:
                return high_el
            if high_el - low_el == 1:
                return high_el if target > nums[low_el] else low_el

            half = math.ceil(high_el - low_el) - 1
            if nums[low_el+half] > target:
                return bs_exact(low_el, low_el+half, nums, target)
            elif nums[low_el+half] < target:
                return bs_exact(low_el + half, high_el, nums, target)
            else:
                return low_el+half

        l1 = nums[:min_idx]
        l2 = nums[min_idx:]

        # print(min_idx)

        i1 = bs_exact(0, min_idx-1, nums, target)
        i2 = bs_exact(min_idx, len(nums)-1, nums, target)
        
        # print(i1, i2)
        if nums[i1] == target:
            return i1
        elif nums[i2] == target:
            return i2
        else:
            return -1
        