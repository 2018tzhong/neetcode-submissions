class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_string = bin(n)
        count = 0
        for digit in binary_string:
            if digit == "1":
                count += 1
        return count