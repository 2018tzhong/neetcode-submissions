class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_counts = {}
        t_counts = {}
        for i in s:
            if i in s_counts:
                s_counts[i] += 1
            else:
                s_counts[i] = 1
        for j in t:
            if j in t_counts:
                t_counts[j] += 1
            else:
                t_counts[j] = 1

        all_chars = set(s_counts.keys()).union(t_counts.keys())
        #print(all_chars)
        for char in all_chars:
            if not char in s_counts:
                return False
            if not char in t_counts:
                return False

            if t_counts[char] != s_counts[char]:
                return False
        return True 