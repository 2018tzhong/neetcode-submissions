class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string = bin(n)
        # print(binary_string)
        bits_only = binary_string[2:].zfill(32)
        reversed_bits = bits_only[::-1]
        return int(reversed_bits, 2)