# 853. Car Fleet

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its speed
        pair = [(p, s) for p, s in zip(position, speed)]
        
        # Sort cars based on starting position in descending order
        # So we process cars from closest to the target to farthest
        pair.sort(reverse=True)
        
        stack = []  # Stack to keep track of fleet arrival times

        for p, s in pair:
            # Calculate time to reach target from current position with given speed
            time = (target - p) / s
            stack.append(time)

            # If the current car catches up to the previous one (arrives sooner or at same time)
            # They merge into a fleet and we pop the current car's time
            # There should be atleast 2 cars to be able to form fleet so len(st)>=2
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # Current car doesn't form a new fleet

        # The number of fleets that will arrive at the destination
        return len(stack)
    
'''
TC = O(n log n)
| Operation | Cost | 
| Pairing positions and speeds | O(n) | 
| Sorting the cars in reverse order | O(n log n) | 
| Iterating through sorted pairs | O(n) | 
| Stack operations (append/pop) | O(1) per op | 

SC = O(n)
- pair: stores n car (position, speed) tuples → O(n)
- stack: in worst case (no fleets merge), stores n arrival times → O(n
'''