a = list(map(int, input('Nhập mảng: ').split()))
result = list(sum(a[:i]) for i in range(1, len(a)+1))
print('result = ', result)