def bin_search(a_list, lo, hi):
    mid = (lo + hi)//2
    print(mid)
    reply = input()
    if lo > hi:
        return False
    if reply == "CORRECT":
        return mid
    elif reply == "TOO_BIG":
        return bin_search(a_list, lo, mid)
    elif reply == "TOO_SMALL":
        return bin_search(a_list, mid, hi)
    else:
        return reply
    return False


t = int(input())
for test_case in range(1, t+1):
    a, b = [int(x) for x in input().split(" ")]
    case_list = [i for i in range(a+1, b+1)]
    n = int(input())
    bin_search(case_list, a + 1, b + 1)
