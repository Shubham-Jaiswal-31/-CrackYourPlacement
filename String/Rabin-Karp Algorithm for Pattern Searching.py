class Solution:
    def search(self, pat, txt):
        # code here
        d, q = 256, 101
        M, N = len(pat), len(txt)
        i, j, p, t, h = 0, 0, 0, 0, 1
        res = []

        for i in range(M-1):
            h = (h*d) % q

        for i in range(M):
            p = (d*p + ord(pat[i])) % q
            t = (d*t + ord(txt[i])) % q

        for i in range(N-M+1):
            if p == t:
                for j in range(M):
                    if txt[i+j] != pat[j]:
                        break
                    else:
                        j += 1

                if j == M:
                    res.append(i + 1)

            if i < N-M:
                t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q
                if t < 0:
                    t = t+q
        return res
