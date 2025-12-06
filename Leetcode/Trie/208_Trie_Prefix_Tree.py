# 208. Implement Trie (Prefix Tree)

class Node:
    def __init__(self):
        # list of 26 elements, initialized to None, representing possible child nodes
        self.links = [None] * 26
        self.flag = False

    def containsKey(self, ch):
        # converts the letter ch into an index (e.g., 'a' -> 0, 'b' -> 1
        return self.links[ord(ch) - ord('a')] is not None
    
    def put(self, ch, node):
        # Stores a new TrieNode (node) in the position corresponding to ch.
        self.links[ord(ch) - ord('a')] = node
    
    def get(self, ch):
        # Returns the child node corresponding to ch, allowing traversal to deeper nodes.
        return self.links[ord(ch) - ord('a')]

    def setEnd(self):
        self.flag = True
    
    def isEnd(self):    
        return self.flag

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                '''- node: Likely refers to a Node object, representing a node in the trie.
- put(ch, Node()): This suggests that node has a method put() that associates the character ch with a new Node() instance.
'''
                node.put(ch, Node())
            # if char is found or even after not found and then new node is created,
            # we go (stand) at the reference node of the char
            node = node.get(ch)  
        node.setEnd()

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return node.isEnd()

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                return False
            node = node.get(ch)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''
Time Complexity:

Insertion: O(N) where N is the length of the word being inserted. This is because we have to iterate over each letter of the word to find its corresponding node or create a node accordingly.
Search: O(N) where N is the length of the word being searched for. This is because in Trie search we traverse over each letter for the word from the root, checking if the current node contains a node at the index of the next letter. This process repeats until we reach the end of the word or encounter a node without the next letter.
Prefix Search: O(N) where N is the length of the prefix being searched for. Similar to searching for words, in prefix search we also iterate over each letter of the word to find its corresponding node.
Space Complexity: O(N) where N is the total number of characters across all unique words inserted into the Trie. For each character in a word, a new node may need to be created leading to space proportional to the number of characters.
'''