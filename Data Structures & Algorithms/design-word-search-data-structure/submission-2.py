class DictionaryNode:
    def __init__(self, val=None):
        self.val = val
        self.count = 0
        self.children = {}

    def __repr__(self):
        return ("" if not self.val else self.val) + ":" + str(self.children)


class WordDictionary:

    def __init__(self):
        self.root = DictionaryNode(None)

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for i in word:
            if not i in curr_node.children:
                curr_node.children[i] = DictionaryNode(i)
            curr_node = curr_node.children[i]
        curr_node.count += 1

    def search(self, word: str) -> bool:
        curr_word = word
        q = [(self.root, curr_word)]
        # print(self.root)
        while q:
            curr = q.pop()
            if len(curr[1]) == 0:
                # print("getting here for", word)
                return curr[0].count > 0
            if curr[1][0] == ".":
                # add all nodes to the path
                for i in curr[0].children.keys():
                    q.append((curr[0].children[i], curr[1][1:]))
            else:
                # print("getting here", curr[1][0], curr[0].children, word)
                if not curr[1][0] in curr[0].children:
                    continue
                q.append((curr[0].children[curr[1][0]], curr[1][1:]))
        return False
