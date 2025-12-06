# 231. Power of Two
# TC = O(1)
# SC = O(1)
def isPowerOfTwo(self, n: int) -> bool:
        
    #if(n and (n-1) == 0): return True
    #else: return False

    #return n>0 and (n and (n-1)) == 0
    return n > 0 and (n & (n - 1)) == 0

'''
n > 0 - This ensures that the number isn't zero or negative, as powers of two are strictly positive.
(n & (n - 1)) == 0:
- This is the key trick. The expression leverages the binary representation of powers of two. A power of two has exactly one bit set to 1 in its binary form. For example:
- 8 → 1000
- 4 → 0100
- 2 → 0010
- When you subtract 1 from a power of two, all bits after the rightmost 1 flip:
- 8 - 1 = 7 → 0111
- 4 - 1 = 3 → 0011
- 2 - 1 = 1 → 0001
- Doing a bitwise AND operation between ( n ) and ( n-1 ) results in 0 only if ( n ) is a power of two. 
(Check if ith bit is set or not from Striver notes)
- 8 & 7 → 1000 & 0111 = 0000
- 4 & 3 → 0100 & 0011 = 0000
- 2 & 1 → 0010 & 0001 = 0000
- If ( n ) is not a power of two, this operation will result in a non-zero value.
- 6 → 0110, 6 - 1 = 5 → 0101,
6 & 5 = 0100 (non-zero).

'''
'''
Naive Approach
TC = O(log n)
SC = O(1)
We can iteratively divide ( n ) by 2 until we reach 1. If at any point ( n ) isn't evenly divisible by 2, then it's not a power of two.
'''
def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n //= 2
    return True
