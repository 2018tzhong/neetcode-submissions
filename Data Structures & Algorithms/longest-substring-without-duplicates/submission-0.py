from collections import deque, defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # one pass, maintain a subarray
        # when we hit a repeat, pop off the front of the list
        curr_chain = deque([])
        max_length_chain = 0
        curr_char_count = defaultdict(int)
        for i in range(len(s)):
            curr_chain.append(s[i])
            curr_char_count[s[i]] += 1
            while curr_char_count[s[i]] > 1:
                curr_char = curr_chain.popleft()
                curr_char_count[curr_char] -= 1

            max_length_chain = max(max_length_chain, len(curr_chain))

        return max_length_chain