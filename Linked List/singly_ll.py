
class Node:
    """A class to represent a node."""
    #__init__ is the constructor method in Python, called automatically 
    # when an object is created. It initializes the object's attributes.
    def __init__(self, data):
        self.data = data #data variable
        self.next = None #next variable for next position/pointer

class LinkedList:
    """A class to represent a singly linked list."""
    def __init__(self):
        self.head = None

    # 1. Length of a linked list
    def length_of_ll(self):
        cnt = 0
        curr = self.head
        while curr:    # same as curr is not None:
            cnt += 1
            curr = curr.next
        return cnt
    
    # 2. Print Linked List
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end = " -> ")
            curr = curr.next
        print("None")

    # 3a. Insert at the front of the linked list
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node 
        #return self.head
    
    # 3b. Insert before a given node
    def insert_before_node(self, target_data, data):
        if not self.head:
            print("List is empty")
            return
        if self.head.data == target_data:
            self.insert_at_front(data)
            return
        curr = self.head
        while curr.next and curr.next.data != target_data:
            curr = curr.next
        if curr.next:
            new_node = Node(data)
            new_node.next = curr.next
            curr.next = new_node
        else:
            print(f"Node with data {target_data} not found")

    # 3c. Insert after a given node
    def insert_after_node(self, target_data, data):
        if not self.head:
            print("List is empty")
            return
        curr = self.head
        while curr and curr.data != target_data:
            curr = curr.next
        if curr:
            new_node = Node(data)
            new_node.next = curr.next
            curr.next = new_node
        else:
            print(f"Node with data {target_data} not found")

    # 3d. Insert at a specific position
    def insert_at_position(self, position, data):
        if position < 0 or position > self.length_of_ll():
            print("Invalid position")
            return
        if position == 0:
            self.insert_at_front(data)
            return
        curr = self.head
        for _ in range(1, position-1): #0 indexed
            curr = curr.next
        new_node = Node(data)
        new_node.next = curr.next
        curr.next = new_node

    # 3e. Insert at the end of the linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return self.head
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        return self.head
    
    # 4a. Delete at the beginning of the linked list
    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    # 4b. Delete at a specific position
    def delete_at_position(self, position):
        if position < 0 or position > self.length_of_ll():
            print("Invalid position")
            return
        if position == 0:
            self.delete_at_beginning()
            return
        curr = self.head
        for _ in range(position - 1):  #0 based indexing
            curr = curr.next
        curr.next = curr.next.next

    # 4c. Delete at the end of the linked list
    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next: #Only 1 node present
            self.head = None
            return
        curr = self.head
        while curr.next and curr.next.next:  # same as while curr.next.next: 
            curr = curr.next
        curr.next = None

    # 4d. Delete the entire linked list
    def delete_entire_list(self):
        self.head = None

    # 5. Search an element in a linked list (Iterative)
    #TC = O(n) SC = O(1)
    def search_iterative(self, target_data):
        curr = self.head
        while curr:
            if curr.data == target_data:
                return True
            curr = curr.next
        return False
    
    # 5. Search an element in a linked list (Recursive)
    #TC = O(n) SC = O(1)
    def search_recursive(self, node, target_data):
        if not node:
            return False
        if node.data == target_data:
            return True
        return self.search_recursive(node.next, target_data)

    

ll = LinkedList()
ll.insert_at_front(5)
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_end(50)
ll.insert_at_position(1, 15)
ll.print_list()
print("Length:", ll.length_of_ll())
ll.delete_at_position(2)
ll.print_list()
print("Search Iterative (20):", ll.search_iterative(20))
print("Search Recursive (25):", ll.search_recursive(ll.head, 25))
print("3rd Node:", ll.get_nth_node(2))
print("2nd Node from End:", ll.get_nth_from_end(1))
