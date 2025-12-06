# for Garbage collection 
import gc 

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLL:
    # Constructor for empty Doubly Linked List 
    def __init__(self): 
        self.head = None
    # Adding a node at the front of the list

    def push(self, new_data):
        # 1 & 2: Allocate the Node & Put in the data
        nn = Node(data = new_data)
        
        # 3. Make next of new node as head and previous as NULL
        nn.next = self.head  #For 1 node only head is None as defined above
        nn.prev = None
        
        # 4. Change prev of head node to new node
        if(self.head is not None):
            self.head.prev = nn
            
        # 5. move the head to point to the new node
        self.head = nn
    #T.C. = O(1)
    #S.C. = O(1)
        

    # Given a node as prev_node, insert a new node after the given node

    def insertAfter(self, prev_node, new_data):
    
        # Check if the given prev_node is NULL
        if(prev_node is None):
            print("Node doesn't exist in DLL !")
            return
        
        # 1. allocate node  & 
        # 2. put in the data
        nn = Node(data = new_data)
        
        # 3. Make next of new node as next of prev_node
        nn.next = prev_node.next
        
        # 4. Make the next of prev_node as new_node
        prev_node.next = nn
        
        # 5. Make prev_node as previous of new_node
        nn.prev = prev_node
        
        # 6. Change previous of new_node's next node
        if(nn.next is not None):
            nn.next.prev = nn
    #T.C. = O(1)
    #S.C. = O(1)
            

    #Add a node before a given node in a Doubly Linked List
    def insertBefore(self, next_node, new_data):
    
        # Check if the given next_node is NULL
        if(next_node is None):
            print("This node doesn't exist in DLL")
            return
        # 1. Allocate node  & 
        # 2. Put in the data
        nn = Node(data = new_data)

        # 3. Make previous of new node as previous of next_node
        nn.prev = next_node.prev

        # 4. Make the previous of next_node as new_node
        next_node.prev = nn

        # 5. Make next_node as next of new_node
        nn.next = next_node

        # 6. Change next of new_node's previous node
        if(nn.prev is not None):
            nn.prev.next = nn
        else:
            head = nn
    #T.C. = O(1)
    #S.C. = O(1)
            
        
    #Add a node at the end in a Doubly Linked List
    def insert_last(self, new_data):
        # 1. allocate node 
        # 2. put in the data
        nn = Node(data=new_data)
        curr = self.head

        # 3. This new node is going to be the
        # last node, so make next of it as NULL
        nn.next = None

        # 4. If the Linked List is empty, then
        #  make the new node as head

        if(self.head is None):
            nn.prev = None
            self.head = nn
            return
        
        # 5. Else traverse till the last node
        while(curr.next is not None):
            curr = curr.next

        # 6. Change the next of last node
        curr.next = nn

        # 7. Make last node as previous of new node
        nn.prev = curr

    #T.C. = O(n)
    #S.C. = O(1)


    def deleteNode(self, dele):

        #Base case
        if(self.head is None or dele is None):
            return
        
        # If node to be deleted is head node 
        if(self.head == dele):
            self.head = dele.next

        # Change next only if node to be deleted is NOT 
        # the last node 
        if(dele.next is not None):
            dele.next.prev = dele.prev

        # Change prev only if node to be deleted is NOT  
        # the first node 
        if(dele.prev is not None):
            dele.prev.next = dele.next

        # Finally, free the memory occupied by dele 
        # Call python garbage collector 
        gc.collect() 

# Driver program to test the above functions 
  
# Start with empty list 
dll = DoublyLL() 
  
# Let us create the doubly linked list 10<->8<->4<->2 
dll.push(2); 
dll.push(4); 
dll.push(8); 
dll.push(10); 
  
print ("\n Original Linked List",end=' ') 
dll.printList(dll.head) 
  
# delete nodes from doubly linked list 
dll.deleteNode(dll.head) 
dll.deleteNode(dll.head.next) 
dll.deleteNode(dll.head.next) 
# Modified linked list will be NULL<-8->NULL 
print("\n Modified Linked List",end=' ') 
dll.printList(dll.head) 