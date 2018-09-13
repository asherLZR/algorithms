def s(a):
    return a if len(a) <= 1 else s([x for x in a[1:] if x < a[0]]) + [a[0]] + s([x for x in a[1:] if x >= a[0]])