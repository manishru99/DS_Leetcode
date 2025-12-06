#206 Reverse a Linked List
'''
Two approaches
Iterative
Recursive
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative
        #TC = O(n)
        #SC = O(1)
        curr = head
        '''
        while curr.next:
            curr = curr.next
        head = curr
        '''
        prev = None
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        return prev
    '''
    #Recursive solution
    #TC = O(n)
    #SC = O(1)

    def reverse_linked_list(head):
        # Base case:
        # If the linked list is empty or has only one node,
        # return the head as it is already reversed.
        if head is None or head.next is None:
            return head
        
        # Recursive step:
        # Reverse the linked list starting from the second node (head.next).
        new_head = reverse_linked_list(head.next)
        
        # Save a reference to the node following
        # the current 'head' node.
        front = head.next
        
        # Make the 'front' node point to the current
        # 'head' node in the reversed order.
        front.next = head
        
        # Break the link from the current 'head' node
        # to the 'front' node to avoid cycles.
        head.next = None
        
        # Return the 'new_head,' which is the new
        # head of the reversed linked list.
        return new_head
        '''