from collections import defaultdict

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr_count = defaultdict(int)
        left = 0
        curr_min_ops = math.inf
        for idx, val in enumerate(blocks):
            curr_count[val] += 1
            if idx - left + 1> k:
                curr_count[blocks[left]] -= 1
                left += 1
            if idx - left + 1 == k:
                curr_min_ops = min(curr_count["W"], curr_min_ops)
        return curr_min_ops


