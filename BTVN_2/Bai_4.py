a = list(map(int, input('Nhập mảng a: ').split()))
k = int(input('Nhập k: '))

print('result:', sum([a[i+1:].count(k - a[i]) for i in range(len(a))]))