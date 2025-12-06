#739. Daily Temperatures

#Brute force
#TC = O(n**2)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            for j in range(i+1, n):
                #a higher temp found
                if temperatures[j] > temperatures[i]:
                    ans[i] = j-i
                    break
        return ans
        

#Optimized approach
#Loop backwards
#Maintain a stack
#st top temp <= curr temp go on popping them till we find a warmer temp
#Once we find a warmer temp then lesser temp after that wouldn't be warmer for any temp
# FInd diff in indices of top and curr temp which is the ans add to list
# Append curr temp index 
#TC = O(n)
#SC = O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n        
        stack = []

        for i in range(n-1, -1, -1): #right to left O(n)
            # Iterate from right to left
            # Pop indices from the stack where temperatures are less or equal to current
            #As stack is implemented with a list in python
            #stack[-1] is -ve indexing to access last elem in a list
            #which is nothing but the stack top
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            # If the stack is not empty, calculate the difference in indices
            # edge cases if st is empty then there's no warmer temp in coming days
            if stack:
                answer[i] = stack[-1] - i
            
            # Push the current index onto the stack
            stack.append(i)
        
        return answer
'''
Worst case: - If temperatures are strictly decreasing (e.g., [90, 80, 70, 60]), 
each index gets pushed to the stack.
- No temperature is popped until the end — so you store all indices at some point.
'''

# Space optimized
# TC = O(n) 
# SC =  O(1) auxiliary, O(n) total
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n  # Initialize result array with all 0s

        # Traverse from second-last element down to first
        for i in range(n - 2, -1, -1):
            j = i + 1  # Start checking the next day
            
            # While there's no warmer temperature at day j
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    # No warmer day found from index j onward
                    j = n
                    break
                # Jump ahead by the number of days previously computed for j
                j += res[j]
            
            # If we find a warmer day, record the difference in days
            if j < n:
                res[i] = j - i
        
        return res



        