import itertools

def brute_force(d, s):
    count = 0
    for y in (s[i:j] for i, j in itertools.combinations(range(len(s)+1), 2)):
        if int(y) % d == 0:
            count += 1
    return count

if __name__ == '__main__':
    d, s = input().split()
    d = int(d)
    print(brute_force(d, s))