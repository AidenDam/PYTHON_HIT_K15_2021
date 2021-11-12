a, b = input().split()

cnt = 0
for i in range(len(b)):
	if a in b[i:]: cnt += 1
	else: break

print(cnt)