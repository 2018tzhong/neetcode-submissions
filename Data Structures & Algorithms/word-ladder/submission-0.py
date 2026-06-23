class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        letters = "abcdefghijklmnopqrstuvwxyz"
        words = set()
        for word in wordList:
            words.add(word)
        

        min_dist = {}
        q = [(beginWord, 1)]
        visited = set()
        while q:
            curr, d = q.pop(0)
            if curr in min_dist and min_dist[curr] <= d:
                continue
            for i in range(len(curr)):
                for j in letters:
                    new_word = curr[:i] + j + curr[i+1:]
                    if new_word in words:
                        q.append((new_word, d+1))
            min_dist[curr] = d
            visited.add(curr)
            # print(q)
        if endWord in min_dist:
            return min_dist[endWord]
        return 0
