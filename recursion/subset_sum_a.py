
'''
Subset Sums (Geeksforgeeks)
Given a array arr of integers, return the sums of all subsets in the list.  Return the sums in any order.
'''

class Solution:
	def subsetSums(self, arr):
            # code here
            n = len(arr)
            ans = []
            curr = []
            def subsets_sum(arr, index, curr):
                #base case
                if index == n:
                    ans.append(sum(curr))
                    return
                #Pick
                subsets_sum(arr, index+1, curr + [arr[index]])
                
                #Not Pick
                subsets_sum(arr, index+1, curr)
            
            subsets_sum(arr, 0, [])
            return ans