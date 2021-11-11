def xd10(s):
	return '0' in s or '1' in s

def ss10(*s):
	return len(set(map(lambda s: str([i for i, v in enumerate(s) if v in ('0', '1')]), s)) - {'[]'}) - 1

s = input().split()
cnt = 0
for i, v in enumerate(s):
    for j in s[0:i]:
        if(ss10(v, j) == 0):
            cnt += 1

print(len(s) - cnt) 