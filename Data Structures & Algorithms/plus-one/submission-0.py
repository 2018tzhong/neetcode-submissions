from collections import deque

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        results = deque(digits)
        results[-1] += 1
        curr_i = len(digits)-1
        while True:
            if results[curr_i] == 10:
                if curr_i == 0:
                    # append left
                    results[curr_i] = 0
                    results.appendleft(1)
                    break
                else:
                    results[curr_i] = 0
                    results[curr_i-1] += 1
                    curr_i -= 1
            else:
                break
        return list(results)

