s = input()
ans = 0

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        if s.count(s[i:j]) > 1:
            ans = max(ans, j-i+1)

print(ans)