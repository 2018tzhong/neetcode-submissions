class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # two branches of dfs were include idx or not
        # two branches are to close right away or later

        results = []
        def dfs(cur, o_count, c_count):
            if c_count > o_count:
                return
            
            if len(cur) == 2*n:
                if o_count  == c_count:
                    results.append(cur)
                return

            dfs(cur + "(", o_count + 1, c_count)
            dfs(cur + ")", o_count, c_count + 1)
        
        dfs("", 0, 0)
        return results