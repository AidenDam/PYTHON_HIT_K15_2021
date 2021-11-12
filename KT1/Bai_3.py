n = int(input())

lst = list(map(int, input().split()))

res = 0
for i in lst:
	cnt = 0
	for j in range(2, i//2+1):
		if i%j == 0:
			cnt += 1
			if cnt > 1:
				break
	else:
		res += cnt

print(('KHôNG', res)[res != 0])