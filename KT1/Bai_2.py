n = int(input())

lst = list(map(int, input().split()))

res = []
for i in lst:
	s = 0
	for j in range(1, i//2+1):
		if i%j == 0:
			s += j
	if s > i:
		res.append(i)
res.sort()

print(len(res), ' '.join([str(e) for e in res]), sep = '\n')