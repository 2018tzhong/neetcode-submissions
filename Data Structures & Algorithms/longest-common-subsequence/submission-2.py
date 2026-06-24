from collections import Counter
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #   c a t
        # c 1 0 0
        # r 0 0 0
        # a 0 1 0
        # b 0 0 0
        # t 0 0 1
        
        #   c a t
        # c 1 0 0
        # r 1 0 0
        # a 1 1 0
        # b 1 1 0
        # t 1 1 1

        #   b s b b
        # j 0 0 0 0
        # b 1 0 0 0
        # b 1 0 1 0
        # b 1 0 1 1

        #   b s b i n i n m
        # j 0 0 0 0 0 0 0 0
        # m 0 0 0 0 0 0 0 1
        # j 0 0 0 0 0 0 0 0
        # k 0 0 0 0 0 0 0 0
        # b 1 1 2
        # k
        # j
        # k
        # v

        #   b s b i n i n m
        # j 0 0 0 0 0 0 0 0
        # m 0 0 0 0 0 0 0 1
        # j 0 0 0 0 0 0 0 1
        # k 0 0 0 0 0 0 0 1
        # b 1 1 1 1 1 1 1 0
        # k
        # j
        # k
        # v

        match = [[0 for i in range(len(text2))] for i in range(len(text1))]
        grid = [[0 for i in range(len(text2))] for i in range(len(text1))]
        # m1 = [False for i in range(len(text1))]
        # m2 = [False for i in range(len(text2))]
        # t1c = Counter()
        # t2c = Counter()
        for idx1, val1 in enumerate(text1):
            # t1c[val1] += 1
            for idx2, val2 in enumerate(text2):
                # t2c[val2] += 1
                if val1 == val2: # and t2c[val2] <= t1c[val1]:
                    match[idx1][idx2] = 1
        
        grid[0][0] = match[0][0]
        for i in range(1, len(text1)):
            grid[i][0] = max(match[i][0], grid[i-1][0])
        for i in range(1, len(text2)):
            grid[0][i] = max(match[0][i], grid[0][i-1])
        

        for idx1 in range(1, len(text1)):
            # already_matched = False
            for idx2 in range(1, len(text2)):
                if match[idx1][idx2]:
                    grid[idx1][idx2] = grid[idx1-1][idx2-1] + 1
                else:
                    grid[idx1][idx2] = max(grid[idx1-1][idx2], grid[idx1][idx2-1])
        return grid[len(text1)-1][len(text2)-1]