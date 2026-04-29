class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0 for i in range(len(temperatures))]
        s = []
        for i, num in enumerate(temperatures):
            # print(s, i, num)
            while len(s) > 0 and num > s[len(s)-1][0]:
                # print("popping", s)
                last = s.pop()
                results[last[1]] = i - last[1]
            s.append((num, i))
        return results