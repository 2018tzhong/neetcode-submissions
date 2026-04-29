class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff_dict = {}
        for idx in range(len(nums)):
            val = nums[idx]
            diff_val = target-val
            if diff_val in diff_dict:
                idxs = diff_dict[diff_val].append(idx)
                return sorted(diff_dict[diff_val])
            else:
                diff_dict[val] = [idx]
        # should never get here, assuming all inputs have an answer
        return None