# 1046. Last Stone Weight

# TC = O(nlogn) SC = O(n)
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # O(n)
        heapq.heapify(stones) # O(n)

        while len(stones) > 1: # n - 1 times in worst case
            first = heapq.heappop(stones) # log(n)
            second = heapq.heappop(stones) # log(n)
            if second > first:  # as we are dealing with -ve values
                heapq.heappush(stones, first - second) # log(n)

        stones.append(0)  # edge case: if empty 0 is req and in other cases it won't matter
        return abs(stones[0])
    
'''
Time Complexity: O(n logn)
Lets break it down:
- [-s for s in stones] → O(n)
- heapq.heapify(stones) → O(n)
- The while loop runs up to n - 1 times (since we're removing two stones each time):
- Each heappop and heappush takes O(logn)
- So worst-case total = O(n logn)
Final total: O(n logn)

Space Complexity: O(n)
- We're storing all stones in a heap → up to n items
- No auxiliary data structures used
Final space: O(n)
'''

# Brute

# TC = O(n*nlogn)
# SC = O(1)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            cur = stones.pop() - stones.pop()
            if cur: # if not 0
                stones.append(cur)
        return stones[0] if stones else 0