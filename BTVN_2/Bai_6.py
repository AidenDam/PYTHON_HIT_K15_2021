d = {
	4: 'hihi',
	1: 'haha',
	9: 10,
	7: '4 3 2 1'
}

d = dict(sorted(d.items(), key = lambda x: x[0]))

print(d)