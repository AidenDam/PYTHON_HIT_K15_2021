number = input('Nhập số: ')

while len(number) > 1:
	number = str(sum(int(e) for e in number))

print('result:', number)