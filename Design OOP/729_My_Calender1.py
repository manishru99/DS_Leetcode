# 729. My Calender 1

class MyCalendar:
    def __init__(self):
        # Initialize an empty list to store booked events
        # Each event is represented as a tuple (start, end)
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        # Iterate through all previously booked events
        for s, e in self.events:
            # Check if the new event overlaps with an existing one
            # Two intervals (start1, end1) and (start2, end2) overlap if:
            # start1 < end2 and end1 > start2
            '''Why both conditions?
- startTime < e ensures the start of the new event is before the end of the existing event.
- endTime > s ensures the end of the new event is after the start of the existing event.
Both cond required as if 2nd is not checked it can happen the event is non-overlapping and before one of the event.
'''
            if startTime < e and endTime > s:
                return False  # Overlap detected, cannot book this time slot

        # If no overlap was found, add the new event to the list
        self.events.append((startTime, endTime))
        return True  # Successfully booked the new event
'''
Time Complexity
- The book(startTime, endTime) method iterates through all existing events to check for overlaps.
- In the worst case, it compares the new event with every existing event before appending.
- So if there are n events already booked:
- Time Complexity: O(n) per booking operation
🧠 SC- All booked events are stored in self.events as tuples.
- In the worst case, if all bookings are non-overlapping, all are stored.
- Space Complexity: O(n) where n is the total number of successful bookings.
'''

''' Why not use a sorted list?
✅ Pros of a Sorted List
By keeping events sorted by startTime, you could:
- Reduce the number of checks needed when booking a new event
- Potentially apply binary search to find the correct insertion point
- Skip over non-overlapping intervals more efficiently

🤔 So why not always use it?
1. Python Lists Are Not Ideal for Frequent Inserts
- Inserting into a sorted list at the correct position requires O(n) time, because inserting into a list in Python involves shifting elements.
- Even though you could use bisect to find the insertion point in O(logn), the actual insertion itself takes O(n).
2. Overlap Checks Still Required
- Even with a sorted list, you’d still need to check the neighboring intervals for overlap — typically just one before and one after the insertion point.
- So while this is better than linear scans over all events, it’s still not dramatically more efficient unless you have thousands of bookings.
3. Better Alternatives Exist for Scaling
- If you're aiming for more efficient scaling, data structures like balanced binary search trees (SortedList from sortedcontainers, AVL trees, etc.) offer:
- O(logn) inserts
- O(logn) overlap detection
- Maintained order and better performance under heavy load

TL;DR
A sorted list works, but in native Python it offers limited performance benefits due to O(n) insertion. If you want sorted + fast, you’d be better off reaching for SortedList from the sortedcontainers module or building a segment tree or interval tree.
Want to refactor the calendar using SortedList and walk through the performance boost? I’m game if you are 📅⚙️

'''

# Tree Solution
class Tree:
    #Can have a separate class for Tree node
    # But for simplicity I just pass the start and end here 
    def __init__(self, start, end): # Our constructor
        # Maintain 4 things here
        self.left = None
        self.right = None
        self.start = start
        self.end = end
        
    def insert(self, start, end): # My insert method
        # initially a pointer set to just self
        # (Pretty much it's just an instance of this Tree object)
        curr = self
        while True:
            # Either we'll reach a conflict from inside while and return False
            # or we'll insert the node and return true
            if start >= curr.end:
                # if we reach the bottom of the tree we need to insert
                if not curr.right:
                    curr.right = Tree(start, end) # set to new Tree node with given start and end
                    return True
                curr = curr.right
            elif end <= curr.start:
                if not curr.left:
                    curr.left = Tree(start, end)
                    return True
                curr = curr.left
            else:
                return False
            

class MyCalendar:
    def __init__(self):
        # In our constructor to make the above interfaces work, 
        self.root = None # Maintain the root node initially NULL

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root: # if root is empty (for the 1st event)
            # Create a new Tree node with given start end and set that as the root
            self.root = Tree(startTime, endTime)
            return True
        # if not empty insert into this existing tree
        # the insert method is gonna return true or false
        return self.root.insert(startTime, endTime)
    
'''
⏱ Time Complexity
Each call to book(startTime, endTime) performs an insertion into a Binary Search Tree (BST), where each node represents a non-overlapping event interval. 
In the worst case, it walks from the root to a leaf to find the correct insertion point.
- Best/Average Case (Balanced Tree):
O(log n) — where n is the number of events already booked
This happens when the tree remains roughly balanced.
- Worst Case (Unbalanced Tree):
O(n) — if events are added in sorted order (e.g. always later in time), the tree becomes skewed (like a linked list)
So, performance depends heavily on the insertion order of events. For robust O(log n), you’d need a self-balancing BST like an AVL or Red-Black Tree.

🧠 Space Complexity
- Each successful booking adds a new Tree node.
- So, for n non-overlapping events booked:
- Space Complexity: O(n)
This includes both the tree structure and the call stack if recursion were used (but in your case, it's iterative — which is space efficient).
'''