def Remove(lst, x):
	lst.remove(x)

def RemoveAll(lst, x):
	while x in lst:
		lst.remove(x)

def Add(lst, x, y):
	if y < 0 or y >= len(lst):
		print("Không chèn được")
	else:
		lst.insert(y, x)

lst = list(map(int , input().split()))

Remove(lst, 1)

print(lst)

RemoveAll(lst, 1)

print(lst)

Add(lst, 2, 3)

print(lst)