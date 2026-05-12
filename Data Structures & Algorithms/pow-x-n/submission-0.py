class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        total = x
        for i in range(abs(n)-1):
            total *= x
        
        if n < 0:
            return 1.0/total
        else:
            return total
