# Job Sequencing Problem (GFG)

# Delay the job to the last possible time slot to maximize profit.
# The job with the maximum profit should be scheduled first.
'''
Input: N = 4, Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output: 2 60
'''
# Greedy Approach

# TC = O(nlogn) + O(n*m) for sorting the jobs in decreasing order of profit. O(N*M) since we are iterating 
# through all N jobs and for every job we are checking from the last deadline, say M deadlines in the worst case.
# SC = O(m) for an array that keeps track of which day job is performed if M is the maximum deadline available.

class job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline # Deadline of the job
        self.profit = profit # Profit of then job
    
class Solution:
    def JobScheduling(self, arr):
        n = len(arr) # arr is a list of job objects
        # Sort the jobs in descending order of profit
        arr.sort(key=lambda x: x.profit, reverse=True)
        
        # Initialize an array to keep track of free time slots
        result = [False] * n
        
        # Initialize variables to store the total profit and number of jobs done
        job_count = 0
        total_profit = 0
        
        # Iterate through all jobs
        for i in range(n):
            # Find a free time slot for this job (if possible)
            for j in range(min(n - 1, arr[i].deadline - 1), -1, -1):
                if not result[j]:
                    result[j] = True  # Mark this slot as occupied
                    job_count += 1  # Increment the count of jobs done
                    total_profit += arr[i].profit  # Add the profit of this job
                    break
        
        return [job_count, total_profit]  # Return the total number of jobs and total profit

