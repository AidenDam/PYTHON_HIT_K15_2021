a = list(map(lambda x: int(x[1:-1]), input('Nhập chuỗi: ').split(',')))

l = 0
r = len(a) - 1
while l <= r:
	while l < r and a[l] % 2 == 0: l += 1
	while l < r and a[r] % 2 == 1: r -= 1
	
	a[l], a[r] = a[r], a[l]
	l += 1
	r -= 1

print(tuple(a))