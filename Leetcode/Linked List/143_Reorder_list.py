# 143. Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach 1 (using an auxiliary list)
# TC = O(n) + O(n) traverse list once to store all nodes, 
# i and j in total move n times
# SC = O(n) for nodes arr
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1
        nodes[i].next = None
        
# Approach 2

