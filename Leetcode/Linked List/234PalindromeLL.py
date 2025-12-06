#234. Palindrome Linked List

from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #stack works better than deque here
        #Brute
        #TC = O(2n)
        #SC = O(n)
        temp = head
        st = deque()
        while temp:
            st.append(temp.val)
            temp = temp.next
        temp = head
        while temp:
            if temp.val != st.pop():
                return False
            temp = temp.next
        return True
    '''
    


    #optimal
    #TC = O(n/2 + n/2 + n/2 + n/2) = O(2n)
    #SC = O(1)

    def reverse_ll(self, head):
        #If reverse method is called for a 2 size original LL
        #which implies the half will have 1 size
        '''
        #recursive
        if not head or not head.next:
            return head
        n_head = self.reverse_ll(head.next)
        front = head.next
        front.next = head
        head.next = None
        return n_head
        '''
        #iterative
        if not head or not head.next:
            return head
        curr = head
        prev = None
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        return prev
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #1 node
        if not head.next:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next: #TC = O(n/2)
            slow = slow.next
            fast = fast.next.next
        #slow is at n/2 pos
        n_head = self.reverse_ll(slow.next)   #TC = O(n/2)
        first = head
        second = n_head
        while second:           #TC = O(n/2)
            if first.val != second.val:
                self.reverse_ll(n_head)  #TC = O(n/2)
                return False
            first = first.next
            second = second.next
        self.reverse_ll(n_head)
        return True
    
