class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Brute force
        #binary search inside each list (ie accessing each row and searching)
        '''
        m = len(matrix) #num of rows
        n = len(matrix[0]) if m>0 else 0#num of cols
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False
        #TC = O(n**2)

        #Approach 2
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n]:
            # or use binary search below
                for j in range(n):
                    if matrix[i][j] == target
                    return True
        return None
        '''
#To achieve O(log(m⋅n)) time complexity, we can treat the 2D matrix as a flattened 1D sorted array and perform a binary search. The key idea is to map the indices of the flattened array back to the 2D matrix.
        #Optimized approach
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1

        while low <= high:
            mid = low + (high - low)//2
            #Map mid to 2D indices:
            row = mid // n
            col = mid % n
            
            if target == matrix[row][col]:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

#TC = O(log(m.n))
#SC = O(1)
            