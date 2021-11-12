def read(s):
	# input 1 chuoi
	# ouput chuoi duoc doc

	res = ''
	i = j = 0
	while i < len(s):
		while j < len(s) and s[i] == s[j]: j += 1
		res += str(j-i) + s[i]
		i = j
	return res

s, n = input().split()

for i in range(int(n)):
	s = read(s)

print(s)