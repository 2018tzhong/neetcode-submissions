from collections import defaultdict

class PrefixNode:
    def __init__(self, val=None):
        self.val = val
        self.count = 0
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for i in word:
            if not i in curr_node.children:
                curr_node.children[i] = PrefixNode(i)
            curr_node = curr_node.children[i]
        curr_node.count += 1

    def search(self, word: str) -> bool:
        curr_node = self.root
        for i in word:
            if not i in curr_node.children:
                return False
            curr_node = curr_node.children[i]
        return curr_node.count > 0

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for i in prefix:
            if not i in curr_node.children:
                return False
            curr_node = curr_node.children[i]
        return True