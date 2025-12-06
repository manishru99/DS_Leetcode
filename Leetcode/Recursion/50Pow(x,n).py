#50. Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        #if n is -ve
        #convert nn to +ve
        nn = abs(n)
        while nn > 0:
            #odd power
            if nn % 2 == 1:
                ans *= x
                nn -= 1
            #even power
            else:
                x *= x
                nn //= 2
        #If n was -ve ans is 1/ans
        if n < 0:
            ans = 1.0 / ans
        
        return ans
#problem size is reduced by half in each iteration of the while loop
#TC = O(logn)
#SC = O(1)

#By recursion
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        
        # Recursive case
        half = self.myPow(x, n // 2)
        
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
'''
TC = O(logn)
SC = O(logn)
Base Case: If n is 0, return 1 (since any number to the power of 0 is 1).
Negative Exponents: If n is negative, convert x to its reciprocal and n to its positive counterpart.
Recursive Case: Compute myPow(x, n // 2) and store it in half.
Even and Odd Exponents:
If n is even, return half * half.
If n is odd, return half * half * x.
'''
