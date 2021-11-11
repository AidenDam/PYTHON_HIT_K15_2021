s = input('Nhập chuỗi: ')

one = s.count('1')

if one % 2 == 1 or one == 0:
	print('NO')
else:
	cnt = 0
	for i in range(len(s)):
		if s[i] == '1':
			cnt += 1
			if(cnt == one/2):
				print(s[:i+1], s[i+1:])
				break