class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbol_map = {"(": ")", "[":"]", "{": "}"}
        for i in s:
            if i in ("(", "[", "{"):
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                last_el = stack.pop()
                if not last_el in symbol_map or symbol_map[last_el] != i:
                    return False
        return len(stack) == 0 
                