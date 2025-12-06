

# Node class represents each entry in the doubly linked list
class Node:
    def __init__(self, key, val):
        self.key = key               # Stores the key
        self.val = val               # Stores the corresponding value
        self.prev = None             # Pointer to the previous node
        self.next = None             # Pointer to the next node

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity          # Maximum capacity of the cache
        self.cache = {}              # Hash map to store key -> node mappings
        #- The dictionary cache holds mappings from keys to their corresponding nodes in the doubly linked list.


        # Initialize dummy head and tail nodes to avoid edge-case checks
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Adds a new node right after the head (most recently used position)
    def _add_node(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    # Removes a node from its current position in the list
    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Fetches a value from the cache and updates its usage order
    def get(self, key: int) -> int:
        if key in self.cache:   # key present in hash
            node = self.cache[key]  # get the val
            # Move the accessed node to the front (most recently used)
            self._remove_node(node)
            self._add_node(node)
            # Update its position in the hash map
            self.cache[key] = self.head.next  # cache[key] access the node in O(1) time via key as 'key'
            return node.val
        return -1  # Key not found

    # Inserts a new key-value pair or updates an existing one
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node if key already exists
            existing_node = self.cache[key]  # getting ind ?
            self._remove_node(existing_node)
            del self.cache[key]
            '''
            what's stored in self.cache[key]?
👉 It’s a reference to the Node instance with:
- key: the cache key (e.g. 5)
- val: the value associated with that key (e.g. 42)
- prev & next: pointers that connect it to other nodes in the doubly linked list
            '''

        if len(self.cache) == self.cap:
            # Evict the least recently used item (node before the tail)
            lru = self.tail.prev
            self._remove_node(lru)
            del self.cache[lru.key]
            '''- Delete its key from the cache dictionary (which gives you fast access).
- Remove the node from the list itself, which is done right after.
            '''

        # Add the new node as most recently used
        new_node = Node(key, value)
        self._add_node(new_node)
        self.cache[key] = self.head.next