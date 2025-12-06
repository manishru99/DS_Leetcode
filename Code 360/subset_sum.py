'''Problem statement
You are given an array 'A' of 'N' integers. You have to return true if there exists a subset of elements of 'A' that sums up to 'K'. Otherwise, return false.



For Example
'N' = 3, 'K' = 5, 'A' = [1, 2, 3].
Subset [2, 3] has sum equal to 'K'.
So our answer is True.'''
from typing import *

def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    n = len(a)
    #Recursive sol
    #TC = O(2^n)
    #The above solution may try all subsets of the given set in worst case. Therefore time complexity of the above solution is exponential. The problem is in-fact NP-Complete (There is no known polynomial time solution for this problem).
    #SC = O(n)
    #base
    if k == 0:
        return True
    if n == 0:
        return False
    #last elem greater than k
    if a[n-1] > k:
        return isSubsetPresent(n-1, k, a)
    #Not take and take
    return (isSubsetPresent(n-1, k, a) or isSubsetPresent(n-1, k-a[n-1], a))
    


#Just print 1 subsequence whose sum is k and then stop.
#Refer subset_sum1.py

'''
def isSubsetPresent(n: int, k: int, a: List[int]) -> bool:
    # Base cases
    if k == 0:
        return True
    if n == 0:
        return False
    
    # If the last element is greater than k, ignore it
    if a[n-1] > k:
        return isSubsetPresent(n-1, k, a)
    
    # Check if the subset can be found by including or excluding the last element
    if isSubsetPresent(n-1, k-a[n-1], a):
        print(a[n-1], end=' ')
        return True
    if isSubsetPresent(n-1, k, a):
        return True
    
    return False
'''

