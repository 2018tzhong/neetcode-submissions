class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_idx = {}
        for idx, val in enumerate(nums):
            if val in last_idx:
                if idx - last_idx[val] <= k:
                    print(last_idx)
                    return True
            last_idx[val] = idx
        return False