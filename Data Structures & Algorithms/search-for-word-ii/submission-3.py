class TrieNode:
    
    def __init__(self, val=None):
        self.val = val
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr_node = self.root
        for i in word:
            if not i in curr_node.children:
                curr_node.children[i] = TrieNode(i)
            curr_node = curr_node.children[i]
        curr_node.count += 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for i in words:
            trie.addWord(i)
        
        final_results = set()
        q = [] # curr_node, coordinate, path, seen
        max_y, max_x = len(board)-1, len(board[0])-1
        for i in range(len(board)):
            for j in range(len(board[0])):
                q.append((trie.root, (i, j), "", set()))
        
        while q:
            curr_node, curr_coordinate, curr_path, curr_seen = q.pop()
            # print("x, y", curr_coordinate[0], curr_coordinate[1])
            # print(curr_node, curr_coordinate, curr_path, curr_seen)
            curr_letter = board[curr_coordinate[0]][curr_coordinate[1]]
            if curr_letter in curr_node.children:
                next_node = curr_node.children[curr_letter]
                if next_node.count > 0:
                    final_results.add(curr_path+curr_letter)
                neighbors = self.getValidNeighborSquares(max_x, max_y, curr_coordinate, curr_seen)
                # print("neighbors ", curr_path + curr_letter, neighbors)
                curr_seen.add(curr_coordinate)
                for i in neighbors:
                    q.append((next_node, i, curr_path + curr_letter, set(curr_seen)))
            else:
                continue

        return list(final_results)

    def getValidNeighborSquares(self, max_x, max_y, coordinate, seen):
        candidates = []
        results = []
        if coordinate[0] > 0:
            candidates.append((coordinate[0]-1, coordinate[1]))
        if coordinate[0] < max_y:
            candidates.append((coordinate[0]+1, coordinate[1]))
        if coordinate[1] > 0:
            candidates.append((coordinate[0], coordinate[1]-1))
        if coordinate[1] < max_x:
            candidates.append((coordinate[0], coordinate[1]+1))
        for i in candidates:
            if not i in seen:
                results.append(i)
        return results