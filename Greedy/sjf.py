# Shortest Job first

# My solution
# TC = O(nlogn) + O(n) = O(nlogn) (Dominated by sorting step)
# SC = O(1)
def solve(self, bt):
    # Code here
    n = len(bt)
    bt.sort() # nlogn
    curr_wt = 0
    curr_wt_sum = 0
    
    for i in range(1, n):
        curr_wt += bt[i-1] 
        curr_wt_sum += curr_wt
    return curr_wt_sum // n # avg wt

