class Solution:
    class TrieNode:
        def __init__(self):
            self.child = [None] * 26
            self.isEnd = False

    class Trie:
        def __init__(self):
            self.root = Solution.TrieNode()

        def insert(self, s: str):
            curr = self.root
            for char in s:
                index = ord(char) - ord('a')
                if not curr.child[index]:
                    curr.child[index] = Solution.TrieNode()
                curr = curr.child[index]
            curr.isEnd = True

        def dfs(self, s: str, curr, vec: list):
            if curr.isEnd:
                vec.append(s)
            for i in range(26):
                if curr.child[i]:
                    self.dfs(s + chr(i + ord('a')), curr.child[i], vec)

        def findit(self, pre: str):
            curr = self.root
            for char in pre:
                idx = ord(char) - ord('a')
                if not curr.child[idx]:
                    return ["0"]
                curr = curr.child[idx]
            vec = []
            self.dfs(pre, curr, vec)
            return vec

    def displayContacts(self, n: int, contact: list, s: str):
        ans = []
        trie = self.Trie()
        for i in range(n):
            trie.insert(contact[i])
        for i in range(len(s)):
            ans.append(trie.findit(s[:i+1]))
        return ans
