#1726. Tuple with Same Product

#Not working
from itertools import combinations
from typing import List
class Solution:
    '''
    def tupleSameProduct(self, nums: List[int]) -> int:
        #find all possible tuples of size 4
        lst = list(combinations(nums, 4))
        ans = 0
        for comb in lst:
            a, b, c, d = comb
            # Condition
            if (a * b) == (c * d):
                ans += 1
        return ans
    '''
    #Approach 2:
    #TC = O(n^2)
    # SC = O(n^2) 
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        product_cnt = defaultdict(int) #used hashing
        # Count the frequency of each product
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                product_cnt[product] += 1 #storing freq at that product
        # Calculate the number of tuples
        tuples_cnt = 0
        for cnt in product_cnt.values():
            #if cnt > 1 only then
            if cnt > 1:
                #Increment tuple_cnt as it is a valid tuple
                #The formula \(\frac{n(n-1)}{2}\) represents the number of ways to choose \(2\) objects from a set of \(n\) objects, where order does not matter.
                #multiply by 8 to account for the arrangements.
                #Explanation:
                #Choose 2 pairs that satisfy a*b == c*d
                #They can be arranged in 8 different ways 4C2 ways
                ##We need to arrange pairs ie {a,b} and {c,d}
                '''
                (a, b, c, d)
(b, a, c, d)
(a, b, d, c)
(b, a, d, c)
(c, d, a, b)
(c, d, b, a)
(d, c, a, b)
(d, c, b, a)
                '''

                tuples_cnt += ((cnt * (cnt-1)) // 2) * 8
        return tuples_cnt

'''
Number of Ways to Choose 2 Pairs:

If a product appears (k) times, the number of ways to choose 2 pairs from these (k) pairs is given by the combination formula:

(2k​)=2k×(k−1)​


Number of Arrangements for Each Pair:

Each pair ((a, b)) can be arranged in 2 ways: ((a, b)) and ((b, a)).
Similarly, each pair ((c, d)) can be arranged in 2 ways: ((c, d)) and ((d, c)).



Number of Ways to Match Two Pairs:

The two pairs ((a, b)) and ((c, d)) can be matched in 2 ways: ((a, b)) with ((c, d)) and ((a, b)) with ((d, c)).



Total Number of Arrangements:

Therefore, the total number of ways to arrange two pairs is:

2×2×2=8


Combining Everything:

The total number of valid tuples ((a, b, c, d)) for a product that appears (k) times is:

(2k​)×8=2k×(k−1)​×8
'''