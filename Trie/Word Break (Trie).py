class Trie:
    def __init__(self, words=[]):
        self.root = {}
        
        for word in words:
            self.add(word)
    
    def add(self, word):
        word += '$'
        curr = self.root
        
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
    
    def isPrefix(self, word):
        word += '$'
        curr = self.root
        
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        
        return True

class Solution:
    def solve(self, word, n, trie, i, memo):
        if i == n:
            return True
        if i in memo:
            return memo[i]
        
        for j in range(i+1, n+1):
            if trie.isPrefix(word[i:j]) and self.solve(word, n, trie, j, memo):
                memo[i] = True
                return True
        
        memo[i] = False
        return False
        
    def wordBreak(self, A, B):
        n = len(A)
        trie = Trie(B)
        memo = {}
        return self.solve(A, n, trie, 0, memo)
