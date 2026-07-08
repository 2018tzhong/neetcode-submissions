class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        results = 0
        curr_sum = 0
        for idx, val in enumerate(arr):
            curr_sum += val
            if idx - left + 1 == k:
                if curr_sum / k >= threshold:
                    results += 1
                curr_sum -= arr[left]
                left += 1
        return results
