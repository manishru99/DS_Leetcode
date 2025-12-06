# 141. Linked List Cycle

#Brute
#TC = O(n) 
# SC = O(n) for hashmap        
def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        mpp = set()
        while curr: #O(n)
            #If already exists in mpp it's a cycle          
            if curr in mpp: #O(1)
                return True
            #Store in the mpp
            mpp.add(curr)
            curr = curr.next
        #If reached Null loop doesn't exist
        return False

#Optimized
#TC = O(n)
#SC = O(1)
def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        #fast ends at NULL for even length list
        #and at last elem for odd length list
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True #cycle exists
    return False #linear list