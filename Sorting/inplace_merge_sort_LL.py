# In-place Merge Sort for Linked List

'''
- Time Complexity: O(N log N), due to recursive sorting and merging.
- Space Complexity: O(log N), for recursive function calls (no extra arrays used).

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to find the middle of the linked list
def getMiddle(head):
    if not head or not head.next:
        return head
    
    slow, fast = head, head.next  # Fast pointer starts ahead to split correctly
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    middle = slow.next  # Middle node
    slow.next = None  # Split the list into two halves
    return middle

# Function to merge two sorted linked lists
def mergeSortedLists(left, right):
    dummy = ListNode()  # Dummy node to start merged list
    tail = dummy
    
    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    
    # Append remaining nodes from either list
    tail.next = left if left else right
    return dummy.next

# Merge Sort function for linked list
def mergeSort(head):
    if not head or not head.next:
        return head  # Base case: single node or empty list
    
    mid = getMiddle(head)  # Get middle node
    left = mergeSort(head)  # Recursively sort left half
    right = mergeSort(mid)  # Recursively sort right half
    
    return mergeSortedLists(left, right)  # Merge both sorted halves

# Helper function to print linked list
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage
if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    
    print("Original List:")
    printList(head)
    
    sorted_head = mergeSort(head)
    
    print("Sorted List:")
    printList(sorted_head)

'''
Key Reason: Sorting in Place
Merge Sort for linked lists works in place because:
- No Extra Array Required: When merging two sorted linked lists, you don’t need a temporary array to store merged elements. Instead, you directly adjust the next pointers of the nodes.
- Recursive Approach Modifies the Original List: Since linked lists allow easy pointer manipulation, recursive calls break the list into halves without additional space.
- Efficient Merging: Unlike arrays that require copying elements into new memory locations, linked lists only require pointer adjustments, avoiding extra storage.
How It Works
- Find the Middle: Use the slow-fast pointer technique to split the list into two halves.
- Recursively Sort Both Halves: This ensures each half is sorted before merging.
- Merge Using Pointers: Instead of creating new nodes, you adjust the next pointers to reorder elements in-place.
'''

'''
Merge Sort for External Sorting
External sorting is used when the dataset is too large to fit into main memory (RAM) and must be processed using disk-based operations. Merge Sort is an ideal choice for external sorting because of its ability to efficiently divide and merge large chunks of data.
How Merge Sort Works for External Sorting
- Divide the Data into Chunks:
- Write Sorted Chunks to Disk:
(Once sorted, each chunk is saved back to disk as a sorted subfile.)
- Merge Sorted Chunks Using Multi-way Merge:
- Repeat Until a Fully Sorted File is Produced:
'''