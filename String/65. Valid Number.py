class Solution:
    def isNumber(self, s: str) -> bool:
        digitSeen, eSeen, dotSeen = False, False, False
        countPlusMinus = 0
        n = len(s)
        for i in range(n):
            c = s[i]
            if c.isdigit():
                digitSeen = True
            elif c in '+-':
                if countPlusMinus == 2:
                    return False
                if i > 0 and (s[i -1] not in 'eE'):
                    return False
                if i == n - 1:
                    return False
                countPlusMinus += 1
            elif c == '.':
                if eSeen or dotSeen:
                    return False
                if i == n - 1 and not digitSeen:
                    return False
                dotSeen = True
            elif c in 'eE':
                if eSeen or not digitSeen or i == n - 1:
                    return False
                eSeen = True
            else:
                return False
        return True
            