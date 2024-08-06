# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        ans = []
        q = deque()
        q.append(root)

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    parent[cur.left.val] = cur
                    q.append(cur.left)
                if cur.right:
                    parent[cur.right.val] = cur
                    q.append(cur.right)

        visited = {}
        q.append(target)
        while k > 0 and q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                visited[cur.val] = 1

                if cur.left and cur.left.val not in visited:
                    q.append(cur.left)

                if cur.right and cur.right.val not in visited:
                    q.append(cur.right)

                if cur.val in parent and parent[cur.val].val not in visited:
                    q.append(parent[cur.val])
            k -= 1
        while q:
            ans.append(q.popleft().val)

        return ans