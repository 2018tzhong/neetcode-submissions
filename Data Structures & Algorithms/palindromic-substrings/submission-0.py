class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # all single letters are considered palindromes
        count = len(s)
        for i in range(len(s)):
            count += self.palindromeProcess(i, i, s)
        for i in range(len(s)-1):
            count += self.palindromeProcess(i, i+1, s)
        return count


    def palindromeProcess(self, i, j, s):

        palSeq = ""
        count = 0
        while i >= 0 and j < len(s):

            if s[i] != s[j]:
                break
            elif i == j:
                # palSeq = s[i]
                pass
            else:
                # palSeq = s[i] + palSeq + s[j]
                count += 1
            i-=1
            j+=1
        return count
        