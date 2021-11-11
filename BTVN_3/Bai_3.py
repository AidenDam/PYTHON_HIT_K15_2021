arr1 = set(input('Enter rally 1: ').split())
arr2 = set(input('Enter rally 2: ').split())

print('result:', ('No', 'Yes')[arr1 == arr1&arr2])