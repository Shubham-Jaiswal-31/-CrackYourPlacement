class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [1] * (n + 1)

        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                l = root - 1
                r = nodes - root
                total += numTree[l] * numTree[r]
            numTree[nodes] = total
        return numTree[n]