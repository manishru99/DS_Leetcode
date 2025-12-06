# 138. Copy List with Random Pointer

'''
Hint 1
There is an extra random pointer for each node, and unlike the next pointer,
which points to the next node, the random pointer can point to any rando
node in the list. A deep copy is meant to create completely separate nodes 
occupying different memory. Why can't we build a new list while iterating 
through the original list?

Hint 2
Because, while iterating through the list, when we encounter a node and 
create a copy of it, we can't immediately assign the random pointer's address. 
This is because the random pointer might point to a node that has not yet 
been created. To solve this, we can first create copies of all the nodes in 
one iteration. However, we still can't directly assign the random pointers 
since we don't have the addresses of the copies of those random pointers. 
Can you think of a data structure to store this information? Maybe a hash 
data structure could help.

'''

# Hash Map (Two Pass)
# TC = O(n) + O(n)
# SC = O(n) + O(n)
# For explanation rfr striver sheet
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        if head:
            # create dummy nodes
            temp = head
            mpp = {}
            mpp[None] = None  # Handle null references
            # step 1: Traverse the ll and creating dummy nodes
            # and storing it in hashmap
            while temp:      # 1st pass
                # create a nn with temp's val
                newnode = Node(temp.val)
                # in mpp for temp, copied node is this newnode
                mpp[temp] = newnode
                temp = temp.next
            # step 2: connect next and the random pointers
            temp = head
            while temp:     # 2nd pass
                copynode = mpp[temp]
                # Map copy nodes next as the temp's next
                copynode.next = mpp[temp.next]
                # similarly for random
                copynode.random = mpp[temp.random]
                # move temp to next
                temp = temp.next
            return mpp[head]


# Optimized
# TC = O(3n) SC = O(n)
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # Step 1: Interleave copied nodes between original nodes
    def insertCopyInBetween(self, head):
        temp = head
        while temp:
            nextelem = temp.next  # Store reference to next node
            copy = Node(temp.val)  # Create copy of current node
            temp.next = copy       # Link original node to its copy
            copy.next = nextelem   # Link copy to next original node
            temp = nextelem        # Move to next original node

    # Step 2: Assign correct random pointers to copied nodes
    def connectRandomPointers(self, head):
        temp = head
        while temp:
            copy = temp.next  # Copied node is directly after original
            # If original's random is not null, link copy's random to the copy of original.random
            copy.random = temp.random.next if temp.random else None
            temp = temp.next.next  # Move to next original node (skip over copy)

    # Step 3: Detach copied nodes to form the deep-copied list
    def getDeepCopyList(self, head):
        temp = head
        dummy = Node(-1)  # Dummy head for new list
        res = dummy       # Pointer to build new list
        while temp:
            res.next = temp.next        # Append copy to new list
            temp.next = temp.next.next  # Restore original list's next pointer
            res = res.next              # Move pointer on new list
            temp = temp.next            # Move to next original node
        return dummy.next  # Return head of the copied list

    # Main method that orchestrates the copy process
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None  # Handle empty list
        self.insertCopyInBetween(head)      # Step 1: Interleave copies
        self.connectRandomPointers(head)    # Step 2: Set random pointers
        return self.getDeepCopyList(head)   # Step 3: Extract copied list