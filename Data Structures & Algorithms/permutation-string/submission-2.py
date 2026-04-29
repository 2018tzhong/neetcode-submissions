from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        for i in s1:
            s1_count[i] += 1
        for i in s2:
            s2_count[i] += 1
        # curr_count = defaultdict(int)
        # for r, char in enumerate(s1):
        #     curr_count[char] += 1
        #     if r-l > len(s2)-1:
        #         curr_count[s1[l]] -= 1
        #         if curr_count[s1[l]] == 0:
        #             del curr_count[s1[l]]
        #         l += 1
        #     if curr_count == s2_count:
        #         return True
        # l = 0
        curr_count = defaultdict(int)
        for r, char in enumerate(s2): 
            curr_count[char] += 1
            if r-l > len(s1)-1:
                curr_count[s2[l]] -=1
                if curr_count[s2[l]] == 0:
                    del curr_count[s2[l]]
                l+= 1
            #print(curr_count, s1_count)
            if curr_count == s1_count:
                return True
        return False