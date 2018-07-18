def trouble_sort(a_list):
    done = False
    while not done:
        done = True
        for i in range(len(v)-2):
            if a_list[i] > a_list[i+2]:
                done = False
                a_list[i], a_list[i+2] = a_list[i+2], a_list[i]


t = int(input())
for case in range(1, t+1):
    n = int(input())
    v = [int(x) for x in input().split(" ")]
    if len(v) > 3:
        if len(v) % 3:
            print("Case #" + str(case) + ": OK")
            continue

        biggest = max(v)
        second = v[0]
        for i in range(len(v)):
            if biggest > v[i] > second:
                second = v[i]
        # if biggest != second:

    else:
        if len(v) == 3:
            if v[0] > v[2]:
                v[0], v[2] = v[2], v[0]
            if v[1] < v[0] or v[1] > v[2]:
                print("Case #" + str(case) + ": 1")
                continue
        elif len(v) == 2:
            if v[0] > v[1]:
                print("Case #" + str(case) + ": 1")
                continue
        print("Case #" + str(case) + ": OK")

