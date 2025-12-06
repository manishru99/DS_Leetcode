# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approach 1 (Neetcode)
# TC = O(n)
# SC = O(n) auxiliary list
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return 
        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next
        size = len(nodes)
        ind = size - n
        if ind == 0:
            return head.next
        nodes[ind - 1].next = nodes[ind].next
        return head


# Approach 2 Optimized
# TC = O(n) - overall, it's a single full pass of the list
# SC = O(1)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        # Move the fast pointer n steps ahead
        for i in range(n):
            fast = fast.next

        slow = head
        # Edge case: if fast is None after n steps, the node to remove is the head
        if fast is None:
            return head.next

        # Move both pointers until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # At this point, slow is pointing to the node before the one to remove
        temp = slow.next
        slow.next = slow.next.next  # Skip the nth node from the end
        # If we want to delete use below
        #temp = None
        # Return the updated head of the list
        return head
