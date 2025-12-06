# 134 Gas STation

# Brute Force
'''
Time Complexity = O(n^2)
- Summing gas and cost takes O(N) time.
- Iterating through all stations takes O(N²) in the worst case.
- Worst case: If we start from each station and iterate around the circle, complexity grows to O(N²).
SC = O(1)
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # Step 1: Check if a solution is possible
        # If total gas available is less than total cost required, completing a circuit is impossible
        if sum(gas) < sum(cost):
            return -1
        # Step 2: Try starting from each gas station
        for i in range(n):
            tank = gas[i] - cost[i] # Initialize fuel tank with gas at station i minus cost to next station
            # If the tank is negative, this station cannot be a valid starting point
            if tank < 0:
                continue
            # Step 3: Traverse the circuit starting from station i
            j = (i + 1) % n  # Move to the next station (circular handling)
            while j != i: # Complete the entire circuit until we return to the start station
                tank += gas[j] - cost[j] # Add gas at station j and subtract cost to next station
                # If fuel becomes negative, station i is not a valid starting point
                if tank < 0:
                    break
                j += 1 # Move to the next station
                j %= n  # Keep it within bounds for circular traversal
            # Step 4: If we successfully traverse the full circuit, return the valid start station
            if j == i:
                return i
        # Step 5: If no valid starting station is found, return -1
        return -1

# Greedy
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost): # Not be able to complete the circle
            return -1
        total, start = 0, 0
        for i in range(n):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start

# TC = O(n) SC = O(1)
