def ip():
	global n
	n = int(input())
	lst = list(map(int , input().split()))
	return lst

def cnt(lst):
	lst .sort()

	i = cnt = 1
	dct = {}
	while i<n:
		if(lst[i] == lst[i-1]):
			cnt += 1
		else:
			dct[lst[i-1]] = cnt
			cnt = 1
		i += 1
	dct[lst[-1]] = cnt

	return dct

dct = cnt(ip())

for k in dct:
	print(k, ':', dct[k])