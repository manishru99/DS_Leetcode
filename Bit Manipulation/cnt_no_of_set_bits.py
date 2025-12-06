# Count number of Set Bits
# Hamming bits

class Solution:
    def countSetBits(self, n: int) -> int:
        count = 0
        while n:
            # This operation removes the lowest set bit
            n &= (n - 1)
            count += 1
        return count