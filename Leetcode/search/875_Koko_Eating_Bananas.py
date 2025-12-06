class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        
        while(low != high): # stop when low is equal to high 
            mid = low + (high-low)//2
            # mid is the rate of eating bananas in an hr
            # k is the hours needed for the rate(mid)
            k = self.hours_needed(piles, mid)
            # here we are treating k as the mid for BS
            if k <= h: # Under the deadline 
                '''
                If k <= h: On satisfying this condition, we can conclude that the 
                number mid is one of our possible answers. But we want the minimum number. 
                So, we will eliminate the right half and consider the left half(i.e. high = mid-1).
                '''
                high = mid
            else: # k (hours needed is higher so we find out the higher rate)
                low = mid + 1        
        return low

    
    def hours_needed(self, piles, k):
        '''
        hr = 0 
        for pile in piles:
            hr += (pile + mid - 1) // mid  # This ensures we round up
        return hr
        '''
        hours = 0
        for pile in piles:
            if pile % k == 0:
                hours += pile // k
            else:
                hours += (pile // k) + 1
        return hours


'''
The number of iterations is approximately log2(max(piles))
The hours_needed function iterates over all elements in piles, which takes O(n)
time, where n is the number of piles.
TC = O(n log2(max(piles)))
SC = O(1)
'''