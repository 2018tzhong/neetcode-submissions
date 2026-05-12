class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        curr = n
        while True:
            if curr in s:
                return False
            if curr == 1:
                return True
            s.add(curr)
            curr = self.addSquaredDigits(curr)

    def addSquaredDigits(self, n):
        total = 0
        for i in str(n):
            total += int(i) ** 2
        return total