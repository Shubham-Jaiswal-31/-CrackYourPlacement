class TwoStacks:
    def __init__(self, n = 100):
        self.n = n
        self.stack = [0] * n
        self.t1 = -1
        self.t2 = n
        
    # Function to push an integer into stack 1
    def push1(self, x):
        self.t1 += 1
        self.stack[self.t1] = x

    # Function to push an integer into stack 2
    def push2(self, x):
        self.t2 -= 1
        self.stack[self.t2] = x

    # Function to remove an element from top of stack 1
    def pop1(self):
        if self.t1 == -1:
            return -1
        res = self.stack[self.t1]
        self.t1 -= 1
        return res

    # Function to remove an element from top of stack 2
    def pop2(self):
        if self.t2 == self.n:
            return -1
        res = self.stack[self.t2]
        self.t2 += 1
        return res
