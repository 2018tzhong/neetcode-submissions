class Solution:
    def numDecodings(self, s: str) -> int:
        # 128 => 2
        # 122 => 3
        # 12 => 2
        # 1225 => 1 22 5, 1 2 2 5, 12 2 5, 12 25, 1 2 25, 
        # 1229 => 1 22 9, 1 2 2 9, 12 2 9
        if len(s) == 0:
            return 0
        if s[0] == "0":
            return 0
        memo = [1, 1]
        for i in range(1, len(s)):
            if s[i] == "0":
                # print("in this 0 case for ", s[i], i)
                # check last digit, if not 1 or 2, return 0
                if s[i-1] in ["1", "2"]:
                    memo.append(memo[-2])
                else:
                    return 0
            elif (s[i-1] in ["1", "2"]) and int(s[i-1:i+1]) <= 26:
                # print("in this 26 case for ", s[i], i, s[i-1:i+1])
                # else, check if this with the last digit can be 26
                memo.append((memo[-1] + memo[-2]))
            else:
                # print("in this else case for ", s[i], i, s[i-1:i+1], int(s[i-1:i+1]) <= 26, s[i-1] in [1, 2])
                memo.append(memo[-1])
                
        print(memo)
        return memo[-1]