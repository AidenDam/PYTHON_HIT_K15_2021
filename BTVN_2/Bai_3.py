# a
s1 = input('Nhập chuỗi: ')
while(len(s1) <= 10):
	s1 = input('Nhập lại: ')
print('Length:', len(s1))
print('Chuỗi yêu cầu:', s1[1:6])

# b
s2 = input('Nhập chuỗi: ')
print('Chuỗi hoa: ', s2.upper())
print('Chuỗi thường: ', s2.lower())
print('Chuỗi thay: ', s2.replace('b', 'g'))

# c
s3 = 'hElLo-mY-NAMe-iS-SuZIe'
s3 = ' '.join([e.lower().title() for e in s3.split('-')])
print(s3)