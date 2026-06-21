class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        results = []

        def dfs(idx, curr):
            if idx > len(s):
                return

            if idx == len(s):
                results.append(curr.copy())
                return

            curr.append(s[idx])
            dfs(idx+1, curr)
            curr.pop()

            curr_string_forward = s[idx]
            curr_string_backward = s[idx]
            # print("pre testing", curr_string_forward, curr_string_backward, idx+1, len(curr))
            for i in range(idx+1, len(s)):
                curr_string_forward = curr_string_forward + s[i]
                curr_string_backward = s[i] + curr_string_backward
                # print("testing", i, curr_string_forward, curr_string_backward, curr_string_forward == curr_string_backward)
                if curr_string_forward == curr_string_backward:
                    curr.append(curr_string_forward)
                    dfs(i+1, curr)
                    curr.pop()
            return
        
        dfs(0, [])
        return results