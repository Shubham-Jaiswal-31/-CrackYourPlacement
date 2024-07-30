def canWePlace(xi, dist, c):
	cnt, last = 1, xi[0]
	
	for i in range(1, len(xi)):
		if xi[i] - last >= dist:
			cnt += 1
			last = xi[i]
		if cnt >= c:
			return True
	return False

t = int(input())
for _ in range(t):
	n, c = list(map(int, input().split()))
	xi = []
	for _ in range(n):
		xi.append(int(input()))
	
	xi.sort()
	l, r = 0, xi[n - 1] - xi[0]
	
	while l <= r:
		m = (l + r) // 2
		if canWePlace(xi, m, c):
			l = m + 1
		else:
			r = m - 1
	print(r)
