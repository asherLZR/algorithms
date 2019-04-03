n = int(input())
p = None
possible = True
a = []
for _ in range(n):
    s = input()
    if p is None:
        s = list(s)
        for i in range(len(s)):
            if i == 0 and s[i] == "?":
                s[i] = "1"
            elif s[i] == "?":
                s[i] = "0"
        p = int("".join(s))
        a.append(p)
    elif len(s) < len(str(p)):
        possible = False
    elif len(s) > len(str(p)):
        s = list(s)
        for i in range(len(s)):
            if i == 0 and s[i] == "?":
                s[i] = "1"
            elif s[i] == "?":
                s[i] = "0"
        p = int("".join(s))
        a.append(p)
    else:
        s = list(s)
        a_len = len(a)
        while p < 100_000_000:
            p += 1
            p_list = list(str(p))
            if len(p_list) > len(s):
                possible = False
                break
            match = True
            for i in range(len(s)):
                if s[i] != "?" and p_list[i] != s[i]:
                    match = False
                    break
            if match:
                a.append(p)
                break
        if a_len == len(a):
            possible = False
if possible:
    print("YES")
    for e in a:
        print(e)
else:
    print("NO")