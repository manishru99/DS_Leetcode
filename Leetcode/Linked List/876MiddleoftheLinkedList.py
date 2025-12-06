# 876. Middle of the Linked List


#TC = O(n)
#SC = O(1)
def middleNode(head_lst):
    #Two pointers
    l, r = 0, len(head_lst)-1

    while l < r:
        l += 1
        r -= 1

    return head_lst[l]

head1 = [1,2,3,4,5]
print(middleNode(head1))
head2 = [1,2,3,4,5,6]
print(middleNode(head2))

#Optimized
# TC = O(n/2)
# SC = O(1)
#Tortoise and Hare Algorithm
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head
    while fast and fast.next and slow:
        #fast != NULL for even length list
        #fast.next !=  NULL for odd length list
        slow = slow.next
        fast = fast.next.next
    return slow
