class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        s = []
        for i in tokens:
            if i == "+":
                s.append(s.pop() + s.pop())
            elif i == "-":
                s.append(-s.pop() + s.pop())
            elif i == "*":
                s.append(s.pop() * s.pop())
            elif i == "/":
                second_el = s.pop()
                first_el = s.pop()
                s.append(int(first_el / second_el))
            else:
                s.append(int(i))
        return s.pop()
