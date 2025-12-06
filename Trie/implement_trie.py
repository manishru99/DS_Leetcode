# Implement Trie - II (code ninjas and striver notes)

                            
class Node:
    """
    Define a class for each node in the trie.
    """

    def __init__(self):
        # Array to store links
        # to child nodes
        self.links = [None] * 26
        # Counter for number of words
        # that end at this node
        self.cntEndWith = 0
        # Counter for number of words that
        # have this node as a prefix
        self.cntPrefix = 0

    def contains_key(self, ch):
        """
        Function to check if the
        node contains a specific key.
        """
        # Check if the link corresponding
        # to the character exists
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch):
        """
        Function to get the child node
        corresponding to a key.
        """
        # Return the link corresponding
        # to the character
        return self.links[ord(ch) - ord('a')]

    def put(self, ch, node):
        """
        Function to insert a child node
        with a specific key.
        """
        # Set the link corresponding to
        # the character to the provided node
        self.links[ord(ch) - ord('a')] = node

    def increase_end(self):
        """
        Function to increment the count
        of words that end at this node.
        """
        # Increment the counter
        self.cntEndWith += 1

    def increase_prefix(self):
        """
        Function to increment the count of
        words that have this node as a prefix.
        """
        # Increment the counter
        self.cntPrefix += 1

    def delete_end(self):
        """
        Function to decrement the count of
        words that end at this node.
        """
        # Decrement the counter
        self.cntEndWith -= 1

    def reduce_prefix(self):
        """
        Function to decrement the count of 
        words that have this node as a prefix.
        """
        # Decrement the counter
        self.cntPrefix -= 1


class Trie:
    """
    Define a class for the
    trie data structure.
    """

    def __init__(self):
        """
        Constructor to initialize the
        trie with an empty root node.
        """
        # Create a new root node
        self.root = Node()

    def insert(self, word):
        """
        Function to insert a
        word into the trie.
        """
        # Start from the root node
        node = self.root
        
        # Iterate over each
        # character in the word
        for ch in word:
            # If the character is not
            # already in the trie
            
            if not node.contains_key(ch):
            
                # Create a new node
                # for the character
                node.put(ch, Node())
           
            # Move to the child node
            # corresponding to the character
            
            node = node.get(ch)
            # Increment the prefix
            # count for the node
            node.increase_prefix()
        # Increment the end count
        # for the last node of the word
        node.increase_end()

    def count_words_equal_to(self, word):
        """
        Function to count the number
        of words equal to a given word.
        """
        # Start from the
        # root node
        node = self.root
        # Iterate over each
        # character in the word
        for ch in word:
            # If the character is
            # found in the trie
            if node.contains_key(ch):
                # Move to the child node
                # corresponding to the character
                node = node.get(ch)
            else:
                # Return 0 if the
                # character is not found
                return 0
        # Return the count of
        # words ending at the node
        return node.cntEndWith

    def count_words_starting_with(self, word):
        """
        Function to count the number of
        words starting with a given prefix.
        """
        # Start from the root node
        node = self.root
        # Iterate over each
        # character in the prefix
        for ch in word:
            # If the character is
            # found in the trie
            if node.contains_key(ch):
                # Move to the child node
                # corresponding to the character
                node = node.get(ch)
            else:
                # Return 0 if the
                # character is not found
                return 0
        # Return the count of
        # words with the prefix
        return node.cntPrefix

    def erase(self, word):
        """
        Function to erase
        a word from the trie.
        """
        # Start from the root node
        node = self.root
        # Iterate over each
        # character in the word
        for ch in word:
            # If the character is
            # found in the trie
            if node.contains_key(ch):
                # Move to the child node
                # corresponding to the character
                node = node.get(ch)
                # Decrement the prefix
                # count for the node
                node.reduce_prefix()
            else:
                # Return if the
                # character is not found
                return
        # Decrement the end count
        # for the last node of the word
        node.delete_end()


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    print("Inserting strings 'apple', 'app' into Trie")
    print("Count Words Equal to 'apple':", trie.count_words_equal_to("apple"))
    print("Count Words Starting With 'app':", trie.count_words_starting_with("app"))
    print("Erasing word 'app' from trie")
    trie.erase("app")
    print("Count Words Equal to 'apple':", trie.count_words_equal_to("apple"))
    print("Count Words Starting With 'apple':", trie.count_words_starting_with("app"))
                           
                        