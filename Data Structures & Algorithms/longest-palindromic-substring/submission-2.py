class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        longestPalindrome = s[0]
        longestSeq = 1
        for i in range(len(s)-1):
            palSeq = self.palindromeProcess(i, i, s)
            # print("palprocess result", i, palSeq)
            if len(palSeq) > longestSeq:
                longestSeq = len(palSeq)
                longestPalindrome = palSeq

            if s[i] == s[i+1]:
                print("in this loop")
                palSeq2 = self.palindromeProcess(i, i+1, s)    
                if len(palSeq2) > longestSeq:
                    longestSeq = len(palSeq2)
                    longestPalindrome = palSeq2
                # print("palprocess result consec", i, palSeq)
        
        return longestPalindrome

    def palindromeProcess(self, i, j, s):
        palindromeSeq = ""
        #print("starting palseq", palindromeSeq)
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                return palindromeSeq
            elif i == j:
                palindromeSeq = s[i]
            else:
                palindromeSeq = s[i] + palindromeSeq + s[j]
            i -= 1
            j += 1
        return palindromeSeq