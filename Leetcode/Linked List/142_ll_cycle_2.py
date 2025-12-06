# 142. Linked List Cycle II


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Brute
        '''
        mpp = set()
        curr = head
        while curr:
            if curr in mpp:
                return curr
            mpp.add(curr)
            curr = curr.next
        return None
        '''
        #Optimized
        #TC = O(n) + O(n) detect cycle and find start of cycle
        #SC = O(1)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                #cycle exists
                #Now find the start of the cycle
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast
        return None
        
