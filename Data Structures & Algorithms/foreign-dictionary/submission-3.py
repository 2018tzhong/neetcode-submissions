from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # edge creation using consecutive words

        # topological sort then, with order
        if len(words) == 1:
            return words[0]

        adj_map = defaultdict(list)
        indegrees = defaultdict(int)
        all_letters = set()
        last_word = words[0]
        for i in range(1, len(words)):
            curr_word = words[i]
            if last_word.startswith(curr_word) and last_word != curr_word:
                return ""
            # edge_created = False
            for j in range(min(len(last_word), len(curr_word))):
                lc, cc = last_word[j], curr_word[j]
                if lc != cc:
                    # print("adding edge", lc, cc, last_word, curr_word)
                    adj_map[lc].append(cc)
                    indegrees[cc] += 1
                    break
                
            for c in last_word:
                all_letters.add(c)
            for c in curr_word:
                all_letters.add(c)
            last_word = curr_word
        
        # print(adj_map)
        # print(indegrees)

        q = []
        for k in list(all_letters):
            if indegrees[k] == 0:
                q.append(k)

        order = []
        while q:
            curr = q.pop(0)
            for val in adj_map[curr]:
                indegrees[val] -= 1
                if indegrees[val] == 0:
                    q.append(val)
            order.append(curr)
        if len(order) == len(all_letters):
            return "".join(order)
        return ""
                