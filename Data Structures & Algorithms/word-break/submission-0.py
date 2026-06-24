class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False for i in range(len(s))]
        curr_string = ""
        for i in range(len(s)):
            curr_string += s[i]
            for j in wordDict:
                if curr_string.endswith(j):
                    if (i-len(j) == -1 or (i-len(j) >= 0 and memo[i-len(j)])):
                        memo[i] = True
        return memo[-1]

