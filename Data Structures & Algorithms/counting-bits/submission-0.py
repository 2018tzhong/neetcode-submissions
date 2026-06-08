class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []
        for num in range(n+1):
            counts.append(self.numOnes(num))
        return counts

    def numOnes(self, n:int):
        binary_string = bin(n)
        count = 0
        for digit in binary_string:
            if digit == "1":
                count += 1
        return count