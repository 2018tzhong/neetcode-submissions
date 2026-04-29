class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = "".join(char for char in s if char.isalnum())
        p1 = 0
        p2 = len(clean_text)-1
        while p2 > p1:
            if clean_text[p1].lower() == clean_text[p2].lower():
                p1 += 1
                p2 -= 1
            else:
                return False
        return True