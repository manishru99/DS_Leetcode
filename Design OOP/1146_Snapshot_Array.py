# 1146 Snapshot Array

'''
🧠 if pairs[mid][0] <= snap_id:
We’re checking if the snapshot ID at mid is less than or equal to the one we’re looking for. In other words:
"Is this version valid at or before the requested snapshot?"

If it is, we save it as a potential answer.

✅ res = mid
We remember this index as the most recent value that doesn't exceed snap_id.
But we want to see if there's an even later one still ≤ snap_id, so...

🔍 left = mid + 1
We move the search window to the right, because there might be a more recent matching snapshot.

'''

class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[] for _ in range(length)]  # Stores (snap_id, value) pairs
        self.i = 0  # Current snapshot ID

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.i, val))  # Append change for current snapshot

    def snap(self) -> int:
        self.i += 1
        return self.i - 1  # Return previous snapshot ID

    def get(self, index: int, snap_id: int) -> int:
        pairs = self.arr[index]
        left, right = 0, len(pairs) - 1
        res = -1

        while left <= right:
            mid = (left + right) // 2
            if pairs[mid][0] <= snap_id:
                res = mid      # potential candidate
                left = mid + 1
            else:
                right = mid - 1

        return 0 if res == -1 else pairs[res][1]
    
'''
⏱ Time Complexity
1. __init__(length)
- Initializes an array of empty lists: O(length)
- Time: O(n)
2. set(index, val)
- Appends a (snap_id, val) pair to the list at arr[index]
- Time: O(1) (amortized for append)
3. snap()
- Increments a counter and returns snapshot ID
- Time: O(1)
4. get(index, snap_id)
- Performs binary search on arr[index], which may contain up to s pairs (where s is number of set() calls at that index)
- Time: O(log s)
(in worst case, s = total number of snapshots, if value changes every time)

🧠 Space Complexity
- arr is a list of length n where each entry is a dynamic list of (snap_id, val) pairs
- Let’s say there are m total set() calls → total extra space is O(m)
- So overall:
- Constructor: O(n) for the structure
- Dynamic storage: O(m) over time
- Total: O(n + m)
    
'''