class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []

        results = []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(idx, curr):
            if idx == len(digits):
                results.append(curr)
                return
            
            for char in mapping[digits[idx]]:
                dfs(idx + 1, curr + char)
            return
            
            
        dfs(0, "")
        return results