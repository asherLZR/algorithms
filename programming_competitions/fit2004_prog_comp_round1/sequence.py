import copy

def first(l):
    for i in range(len(l)):
        if i == 0 and l[i] == "?":
            l[i] = "1"
        elif l[i] == "?":
            l[i] = "0"
    return l


def higher(f, m):
    if int("".join(f)) >= m:
        return True
    return False


n = int(input())
a = []
possible = True
p = None
for _ in range(n):
    if not possible:
        continue
    s = list(input())
    if p is None:
        p = first(s)
        a.append(p)
        continue
    elif len(s) < len(p):
        possible = False
    elif len(s) > len(p):
        p = first(s)
        a.append(p)
    else:
        a_len = len(a)
        lo = int("".join(p)) + 1
        tmp = copy.deepcopy(s)
        tmp = first(tmp)
        i = len(s) - 1
        while i > -1:
            if higher(tmp, lo):
                break
            if p[i] == "9":
                i -= 1
                continue
            if s[i] == "?":
                tmp[i] = str(int(p[i]) + 1)
                if higher(tmp, lo):
                    break
                tmp[i] = "0"
            i -= 1
        if higher(tmp, lo):
            p = tmp
            a.append(p)
        else:
            possible = False

if possible:
    print("YES")
    for e in a:
        print(int("".join(e)))
else:
    print("NO")