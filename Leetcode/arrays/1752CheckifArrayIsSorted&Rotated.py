class Solution:
    def check(self, nums: List[int]) -> bool:
        #Brute
        n = len(nums)
        '''
        #Consider all rotations of the arr
        for rotation_offset in range(n): #O(n)
            check_sorted = []
            #1st loop from rot offset to last
            for index in range(rotation_offset, n): #O(n)
                check_sorted.append(nums[index])
            #2nd loop from 1st elem to rot offset
            for index in range(rotation_offset): 
                check_sorted.append(nums[index])

            is_sorted = check_sorted == sorted(check_sorted) #O(n)
            
            #or for sorting code
            is_sorted = True
            for i in range(n-1):
                if check_sorted[index] > check_sorted[index + 1]:
                    is_sorted = False
                    break
            
            if is_sorted:
                return True
        return False
        #TC = O(n^2)
        #SC = O(n)
        
        #Better approach
        #Create a sorted version of the arr
        check_sorted = sorted(nums) #O(nlogn)
        # Compare the original list with the sorted list, considering all possible rotations
        for rotation_offset in range(n): #O(n)
            is_match = True
            for index in range(n): #O(n)
                if nums[(rotation_offset + index) % n] != check_sorted[index]:
                    is_match = False
                    break
            if is_match:
                return True
            
        return False
        #TC = O(nlogn) + O(n^2)
        #SC = O(n)
        '''

        #Optimized
        inv_cnt = 0
        if n == 0 or n == 1:
            return True
        for i in range(n):    #O(n)
            if nums[i] > nums[(i+1) % n]:
                inv_cnt += 1  # For the elem after which the order breaks
                # it can be 1 for a rotated arr or 0 for a sorted arr
        return inv_cnt <= 1

        #TC = O(n)
        #SC = O(1)


