from collections import Counter
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        q = [(Counter(), [])]
        results = []
        num_counts = Counter(nums)
        while q:
            curr_counts, curr = q.pop()
            # if all(curr_counts[k] == num_counts[k] for k in num_counts):
            #     results.append(curr.copy())
            #     continue
            if len(curr) == len(nums):
                results.append(curr.copy())
                continue

            for i in nums:
                if curr_counts[i] < num_counts[i]:
                    curr_counts_copy = curr_counts.copy()
                    curr_counts_copy[i] += 1
                    q.append((curr_counts_copy, curr + [i]))
        return results
