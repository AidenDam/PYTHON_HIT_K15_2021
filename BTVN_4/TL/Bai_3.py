lst = list(map(int , input().split()))

ans = []
for idx, val in enumerate(lst):
	if val%2 == 1:
		print(idx, end = ' ')
	else:
		ans.append(val)

print()
print(ans)