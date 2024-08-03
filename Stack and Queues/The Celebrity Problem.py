class Solution:
    def celebrity(self, mat):
        n = len(mat)
        stack = []
        for i in range(n - 1, -1, -1):
            stack.append(i)
            
        while len(stack) > 1:
            first = stack.pop()
            second = stack.pop()
            if mat[first][second] and not mat[second][first]:
                stack.append(second)
            elif not mat[first][second] and mat[second][first]:
                stack.append(first)
        
        if not stack: return -1
        
        num = stack.pop()
        r = c = 0
        for i in range(n):
            r += mat[num][i]
            c += mat[i][num]
            
        return num if r == 0 and c == (n - 1) else -1