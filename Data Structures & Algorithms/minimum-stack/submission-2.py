class MinStack:

    def __init__(self):
        self.s = []
        self.min_s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        
        if len(self.min_s) == 0 or val <= self.min_s[-1]:
            self.min_s.append(val)

    def pop(self) -> None:
        last_el = self.s.pop()
        if last_el == self.min_s[-1]:
            self.min_s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_s[-1]
