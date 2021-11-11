def MyMathShower(*lst):
	sm = float(sum(lst))
	sb = lst[0]*2 - sm
	mul = 1.0
	for e in lst:
		mul *= e
	print(sm, mul, sb)

MyMathShower(10, 4, 1, 1)