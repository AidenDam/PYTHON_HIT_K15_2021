s = input()

print(s[s.index('(') + 1: s.index(',')], s[s.index(',') + 1: s.index(')')])