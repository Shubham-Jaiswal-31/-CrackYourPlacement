class Solution:
    def countArrangement(self, n: int) -> int:
        visit = [False] * (n + 1)
        self.count = 0

        def calculate(pos):
            if pos > n:
                self.count += 1
            for i in range(1, n + 1):
                if not visit[i] and (pos % i == 0 or i % pos == 0):
                    visit[i] = True
                    calculate(pos + 1)
                    visit[i] = False
        
        calculate(1)
        return self.count