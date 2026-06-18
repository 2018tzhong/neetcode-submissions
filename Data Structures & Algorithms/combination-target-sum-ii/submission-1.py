from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # do the same as other combination sum
        # at the end though check the count of elements
        # q = [(Counter(), 0)]
        # candidate_counts = Counter(candidates)
        # results = set()
        # print(candidate_counts)
        # while q:
        #     els, curr_sum = q.pop()
        #     if curr_sum > target:
        #         continue
        #     elif curr_sum == target:
        #         results.add(tuple(sorted(els.elements())))

        #     for i in candidate_counts.keys():
        #         if curr_sum + i <= target and els[i] < candidate_counts[i]:
        #             els_copy = els.copy()
        #             els_copy[i] += 1
        #             q.append((els_copy, curr_sum + i))
        
        # # eligible_results = []
        # # for combo in list(results):
        # #     counts = Counter(combo)
        # #     if all(counts[k] <= candidate_counts[k] for k in counts):
        # #         eligible_results.append(list(combo))
        # # return eligible_results

        # return [list(i) for i in list(results)]
        # results = set()
        # sorted_candidates = sorted(candidates)

        # def dfs(i, cur, total):
        #     if total == target:
        #         results.add(tuple(cur))
        #         return
        #     for idx in range(i, len(sorted_candidates)):
        #         if idx > i and sorted_candidates[idx] == sorted_candidates[i-1]:
        #             continue
        #         if total + sorted_candidates[idx] > target:
        #             break

        #         cur.append(sorted_candidates[idx])
        #         dfs(idx+1, cur, total+sorted_candidates[idx])
        #         cur.pop()

        # dfs(0, [], 0)
        # return [list(i) for i in list(results)]
        res = []
        candidates.sort()

        def dfs(idx, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, cur + candidates[i])
                path.pop()

        dfs(0, [], 0)
        return res
