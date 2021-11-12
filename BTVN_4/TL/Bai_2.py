s = input()

print((s[:2] + s[-2:], '')[len(s) < 2])