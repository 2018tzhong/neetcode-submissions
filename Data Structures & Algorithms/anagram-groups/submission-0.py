class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []

        hashed_strs = {}
        for i in strs:
            hashed = self.hash_count(i)
            if hashed in hashed_strs:
                hashed_strs[hashed].append(i)
            else:
                hashed_strs[hashed] = [i]
        #print(hashed_strs)
        for k, v in hashed_strs.items():
            groups.append(v)
        return groups

    def hash_count(self, s: str):
        counts = {}
        for i in s:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        
        hashed=""
        for i in sorted(counts.keys()):
            hashed = hashed + i + str(counts[i])
        return hashed