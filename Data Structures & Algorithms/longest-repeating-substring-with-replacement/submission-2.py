from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # keep track of k indexes for characters
        char_count = defaultdict(int)
        max_char_length = 0
        max_chain_length = 0
        left = 0
        for idx, char in enumerate(s):
            char_count[char] += 1
            max_char_length = max(max_char_length, char_count[char])
            # how do we update left?
            # bug is here. we need to actually check what left should be updated to
            # left = max(0, idx - (len(char_count[max_char]) + k))
            while (idx - left + 1) - max_char_length > k:
                char_count[s[left]] -= 1
                left += 1
            max_chain_length = max(max_chain_length, idx-left+1)
            print(max_chain_length, idx-left+1)
        return max_chain_length
            