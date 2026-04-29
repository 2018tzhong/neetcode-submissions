from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = defaultdict(int)
        for i in t:
            t_count[i] += 1
        l = 0
        curr_count = defaultdict(int)
        min_string = s
        substring_found = False
        for r, char in enumerate(s):
            curr_count[char] += 1
            if self.checkCounts(curr_count, t_count):
                substring_found = True
                while self.checkCounts(curr_count, t_count):
                    # then we can update left
                    curr_count[s[l]] -= 1
                    l += 1
                l-= 1
                curr_count[s[l]] += 1
                if r-l+1 <= len(min_string):
                    min_string = s[l:r+1]
        if substring_found:
            return min_string
        else:
            return ""
        

    def checkCounts(self, curr_count, t_count):
        return all(curr_count[k] >= t_count[k] for k in t_count.keys())