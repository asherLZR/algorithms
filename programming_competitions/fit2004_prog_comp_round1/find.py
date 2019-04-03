n = input()
s = input()
set_s = set(s)
d = {}
for e in set_s:
    d[e] = 1
i, j = 0, 0
num_unq = len(set_s)
min_char = float('inf')
while j < len(s):
    j_c = s[j]
    d[j_c] -= 1
    if d[j_c] == 0:
        num_unq -= 1
    j += 1
    while num_unq == 0:
        if j - i < min_char:
            min_char = j - i
        if d[s[i]] == 0:
            num_unq += 1
        d[s[i]] += 1
        i += 1
print(min_char)
