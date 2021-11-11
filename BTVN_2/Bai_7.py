n = int(input('Nhap n: '))

d = dict()
for i in range(n):
	k = input('Key = ')
	d[k] = input('Value = ')

val = list(d.values())
item = list(d.items())
v = set(val)
a = sorted([[val.count(e), e] for e in v])

res = [it[0] for it in item if it[1] == a[-1][1]]

print(' '.join(res))
# print(a)