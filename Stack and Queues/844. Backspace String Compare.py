class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def nextValidChar(str, index):
            backspace = 0
            while index >= 0:
                if backspace == 0 and str[index] != '#':
                    break
                elif str[index] == '#':
                    backspace += 1
                else:
                    backspace -= 1
                index -= 1
            return index
        
        si, ti = len(s) - 1, len(t) - 1
        while si >= 0 or ti >= 0:
            si = nextValidChar(s, si)
            ti = nextValidChar(t, ti)

            char_s = s[si] if si >= 0 else ''
            char_t = t[ti] if ti >= 0 else ''
            if char_s != char_t:
                return False
            si -= 1
            ti -= 1
        return True
        