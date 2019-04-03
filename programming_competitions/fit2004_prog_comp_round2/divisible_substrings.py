# check that every case works for len == 1!!!!

def divisible_substrings(d, s):
    count = 0
    if d == 1:
        count = sum(range(1, len(s)+1))
    elif d == 2:
        for i, digit in enumerate(s):
            if int(digit) in (0, 2, 4, 6, 8):
                count += i+1
    elif d == 3:
        pass
        # 3 3812312
    elif d == 4:
        pass
    elif d == 5:
        for i, digit in enumerate(s):
            if int(digit) in (0, 5):
                count += i+1
    elif d == 6:
        pass
    elif d == 7:
        pass
    elif d == 8:
        pass
    elif d == 9:
        pass
    return count

if __name__ == '__main__':
    d, s = input().split()
    d = int(d)
    print(divisible_substrings(d, s))