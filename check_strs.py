def check_strs(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

s1 = input()
s2 = input()

print(check_strs(s1, s2))
